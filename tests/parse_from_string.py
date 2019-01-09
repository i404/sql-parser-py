from parser import spark

if __name__ == '__main__':
    sql = "create table xxxx as select * from xxx.a limit 1; " \
          "select * from adad.adfas; " \
          "with c as (select * from dw.ss limit 1) select * from c"
    result = spark.parse_string(sql, True)

    print("input tables:")
    for ts in result.input_tables:
        print(ts)

    print("output tables:")
    for ts in result.output_tables:
        print(ts)

    print("details:")
    for statement_result in result.statement_details:
        print("statement content:")
        print(sql[statement_result.start:statement_result.stop])
        print("statement type:")
        print(statement_result.type)

        print("statement input tables:")
        for ts in statement_result.input_tables:
            print(ts)

        print("statement output tables:")
        for ts in statement_result.output_tables:
            print(ts)
