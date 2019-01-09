from parser.spark.base.SparkSqlBaseLexer import *
from parser.spark.base.SparkSqlBaseVisitor import *

if __name__ == '__main__':
    sql = "select 1;select 2 from shit;"
    upper_case_sql = sql.upper()
    upper_case_stream = InputStream(upper_case_sql)
    lexer = SparkSqlBaseLexer(upper_case_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SparkSqlBaseParser(token_stream)

    parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION

    tree = parser.statement()
    print(sql[tree.start.start:tree.stop.stop + 1])
