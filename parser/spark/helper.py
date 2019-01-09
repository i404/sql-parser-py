from antlr4 import *
from .base.SparkSqlBaseLexer import SparkSqlBaseLexer
from .base.SparkSqlBaseParser import SparkSqlBaseParser
from .visitor import SparkSqlVisitor
from ..base_helper import BaseHelper
from ..models  import ContentResult, StatementResult


class SparkSqlHelper(BaseHelper):
    @staticmethod
    def parse_string(sql: str, detail=False):
        sql += ';'
        upper_case_sql = sql.upper()
        sql_length = len(sql)

        spark_sql_visitor = SparkSqlVisitor()
        lexer = SparkSqlBaseLexer()
        parser = SparkSqlBaseParser(None)

        # lexer.removeErrorListeners();
        # parser.removeErrorListeners()
        parser._interp.predictionMode = PredictionMode.SLL

        content_result = ContentResult()
        while upper_case_sql != "":
            upper_case_sql = upper_case_sql.lstrip()
            if upper_case_sql[0] == ';':
                upper_case_sql = upper_case_sql.lstrip(';')
                continue
            sql = sql[-len(upper_case_sql):]

            upper_case_stream = InputStream(upper_case_sql)
            lexer.inputStream = upper_case_stream
            token_stream = CommonTokenStream(lexer)
            parser.setTokenStream(token_stream)

            statement_context = parser.statement()
            next_index = statement_context.stop.stop + 1

            if len(upper_case_sql) != next_index:
                statement_info = spark_sql_visitor.parse(statement_context, sql)
                if detail and statement_info:
                    statement_result = StatementResult()
                    statement_result.start = sql_length - len(sql)
                    statement_result.stop = statement_result.start + next_index
                    statement_result.type = statement_info.statement_type
                    statement_result.input_tables = statement_info.statement_deps.input_tables
                    statement_result.output_tables = statement_info.statement_deps.output_tables

                    content_result.statement_details.append(statement_result)

                upper_case_sql = upper_case_sql[next_index:]
                sql = sql[next_index:]

            semi_index = upper_case_sql.find(";")
            if semi_index != -1:
                upper_case_sql = upper_case_sql[semi_index + 1:]
                sql = sql[semi_index + 1:]
        content_result.input_tables = spark_sql_visitor.statement_deps.input_tables
        content_result.output_tables = spark_sql_visitor.statement_deps.output_tables
        return content_result
