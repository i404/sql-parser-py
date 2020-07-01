from antlr4.tree.Tree import ParseTree
from .base.SparkSqlBaseVisitor import SparkSqlBaseVisitor
from .base import SparkSqlBaseParser
from .base.SparkSqlBaseParser import *
from ..models import STATEMENT_TYPE
from ..models import Table, TableDeps, StatementInfo


class SparkSqlVisitor(SparkSqlBaseVisitor):

    def __init__(self):
        self._insert_token = None
        self._current_opt_type = STATEMENT_TYPE.UNKOWN
        self._current_database = "default"
        self._aliases = set()
        self._sql = ""
        self.statement_table_deps: TableDeps = TableDeps()
        self.single_statement_table_deps: TableDeps = None
        super().__init__()

    def parse(self, tree: ParseTree, sql) -> StatementInfo:
        self._sql = sql
        return self.visit(tree)

    def visit(self, tree: ParseTree) -> StatementInfo:
        self._current_opt_type = STATEMENT_TYPE.UNKOWN
        self._insert_token = None
        self._aliases.clear()
        self.single_statement_table_deps = TableDeps()
        return super().visit(tree)

    def shouldVisitNextChild(self, node, currentResult):
        return currentResult is None

    @property
    def statement_deps(self):
        return self.statement_table_deps

    def _get_real_text(self, start, stop):
        try:
            return self._sql[start:stop + 1]
        except Exception as e:
            return None

    def _get_token_text(self, token):
        return self._get_real_text(token.start.start, token.stop.stop) if token else None

    def visitStatementDefault(self, ctx: SparkSqlBaseParser.StatementDefaultContext):
        if ctx.start.text == "SELECT":
            self._current_opt_type = STATEMENT_TYPE.SELECT
            super().visitQuery(ctx.query())
            return StatementInfo(STATEMENT_TYPE.SELECT, self.single_statement_table_deps)

        elif ctx.start.text == "INSERT":
            super().visitQuery(ctx.query())

            table_context = ctx.query().queryNoWith().getChild(0)

            if isinstance(table_context,
                          (SparkSqlBaseParser.InsertIntoTableContext, SparkSqlBaseParser.InsertOverwriteTableContext)):
                table_identifier = table_context.tableIdentifier()
                table = Table(self._get_token_text(table_identifier.db), self._get_token_text(table_identifier.table))
                self.add_output_table(table)

            if self._current_opt_type == STATEMENT_TYPE.INSERT_VALUES:
                return StatementInfo(STATEMENT_TYPE.INSERT_VALUES, self.single_statement_table_deps)
            else:
                return StatementInfo(STATEMENT_TYPE.INSERT_SELECT, self.single_statement_table_deps)

        elif ctx.start.text == "FROM":
            self._current_opt_type = STATEMENT_TYPE.MULTI_INSERT
            super().visitQuery(ctx.query())
            return StatementInfo(STATEMENT_TYPE.MULTI_INSERT, self.single_statement_table_deps)

        elif ctx.start.text == "WITH":
            super().visitQuery(ctx.query())
            return StatementInfo(STATEMENT_TYPE.WITH, self.single_statement_table_deps)

    def visitNamedQuery(self, ctx):
        super().visitQuery(ctx.query())
        self._aliases.add(self._get_token_text(ctx.identifier()))

    def visitCreateHiveTable(self, ctx: SparkSqlBaseParser.CreateHiveTableContext):
        table_header = ctx.createTableHeader()
        table_identifier = table_header.tableIdentifier()

        table = Table(self._get_token_text(table_identifier.db), self._get_token_text(table_identifier.table),
                      table_header.TEMPORARY() is not None, table_header.EXTERNAL() is not None)

        if ctx.query() is not None:
            super().visitQuery(ctx.query())
            self._current_opt_type = STATEMENT_TYPE.CREATE_TABLE_AS_SELECT
        else:
            self._current_opt_type = STATEMENT_TYPE.CREATE_TABLE

        self.add_output_table(table)
        return StatementInfo(self._current_opt_type, self.single_statement_table_deps)

    def visitUse(self, ctx: SparkSqlBaseParser.UseContext):
        self._current_database = self._get_token_text(ctx.db)

    def visitSingleInsertQuery(self, ctx: SparkSqlBaseParser.SingleInsertQueryContext):
        super().visit(ctx.queryTerm())
        table_context = ctx.insertInto()
        if table_context is not None:
            if isinstance(table_context,
                          (SparkSqlBaseParser.InsertOverwriteTableContext, SparkSqlBaseParser.InsertIntoTableContext)):
                table_identifier = table_context.tableIdentifier()
                if table_identifier is not None:
                    table = Table(self._get_token_text(table_identifier.db),
                                  self._get_token_text(table_identifier.table))
                    self.add_output_table(table)

    def visitTableIdentifier(self, ctx: SparkSqlBaseParser.TableIdentifierContext):
        if (self._current_opt_type == STATEMENT_TYPE.CREATE_TABLE_AS_SELECT or
                self._current_opt_type == STATEMENT_TYPE.SELECT or
                self._current_opt_type == STATEMENT_TYPE.INSERT_SELECT):
            table = Table(self._get_token_text(ctx.db), self._get_token_text(ctx.table))
            self.add_input_table(table)
        elif self._current_opt_type == STATEMENT_TYPE.MULTI_INSERT and "from" == self._insert_token:
            table = Table(self._get_token_text(ctx.db), self._get_token_text(ctx.table))
            self.add_input_table(table)

    def visitInlineTableDefault1(self, ctx: SparkSqlBaseParser.InlineTableDefault1Context):
        self._current_opt_type = STATEMENT_TYPE.INSERT_VALUES

    def visitQuerySpecification(self, ctx: SparkSqlBaseParser.QuerySpecificationContext):
        self._current_opt_type = STATEMENT_TYPE.INSERT_SELECT
        super().visitQuerySpecification(ctx)

    def visitFromClause(self, ctx: SparkSqlBaseParser.FromClauseContext):
        self._insert_token = "from"
        super().visitFromClause(ctx)

    def visitMultiInsertQueryBody(self, ctx: SparkSqlBaseParser.MultiInsertQueryBodyContext):
        self._insert_token = "insert"
        obj = ctx.insertInto()

        if isinstance(obj, (SparkSqlBaseParser.InsertOverwriteTableContext, SparkSqlBaseParser.InsertIntoTableContext)):
            table_identifier = obj.tableIdentifier()
            table = Table(self._get_token_text(table_identifier.db), self._get_token_text(table_identifier.table))
            self.add_output_table(table)

    def add_input_table(self, ts: Table):
        if ts.database is None:
            if ts.database not in self._aliases:
                ts.database = self._current_database
            else:
                return

        if ts not in self.statement_table_deps.output_tables:
            self.statement_table_deps.input_tables.add(ts)

        if ts not in self.single_statement_table_deps.output_tables:
            self.single_statement_table_deps.input_tables.add(ts)

    def add_output_table(self, ts: Table):
        # if ts.database is None:
        #     if ts.database not in self._aliases:
        #         ts.database = self._current_database
        #     else:
        #         return

        if ts.database is None:
            ts.database = self._current_database

        self.statement_table_deps.output_tables.add(ts)
        self.single_statement_table_deps.output_tables.add(ts)
