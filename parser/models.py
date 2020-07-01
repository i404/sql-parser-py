from enum import Enum

STATEMENT_TYPE = Enum("STATEMENT_TYPE",
                      (
                          'CREATE_TABLE',
                          'CREATE_TABLE_AS_SELECT',

                          'SELECT',
                          'INSERT_VALUES',
                          'INSERT_SELECT',
                          'MULTI_INSERT',

                          'USE',
                          'WITH',
                          'UNKOWN'
                      )
                      )


class Table:
    def __init__(self, database=None, table=None, is_temporary=False, is_external=False):
        self.database = database
        self.table = table
        self.is_temporary = is_temporary
        self.is_external = is_external

    def __str__(self):
        full_table_name = "%s.%s" % (self.database, self.table)
        if self.is_temporary:
            full_table_name += "   \033[01;31m<- temporary\033[0m"
        return full_table_name

    def __repr__(self):
        return "Table(%s, %s)" % (self.database, self.table)

    def __eq__(self, other):
        if isinstance(other, Table):
            return (self.database == other.database) and (self.table == other.table)
        else:
            return False

    def __hash__(self):
        return hash(self.__repr__())


class TableDeps:
    def __init__(self):
        self.input_tables = set()
        self.output_tables = set()

    # def add_input_table(self):
    #     pass
    #
    # def add_output_table(self):
    #     pass


class StatementInfo:
    def __init__(self, statement_type: STATEMENT_TYPE = None, statement_deps: TableDeps = None):
        self.statement_deps = statement_deps
        self.statement_type = statement_type


class StatementResult:
    def __init__(self):
        self.start = None
        self.stop = None
        self.type = None
        self.input_tables = None
        self.output_tables = None


class ContentResult:
    def __init__(self):
        self.statement_details: list = []
        # self.content_deps: TableDeps = None
        self.input_tables = None
        self.output_tables = None
