# generate source files
```bash
antlr4 -Dlanguage=Python3 -visitor SparkSqlBase.g4
```

# dependency
```bash
pip3 install antlr4-python3-runtime===4.8
```

# example
```python
from parser import spark
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
```