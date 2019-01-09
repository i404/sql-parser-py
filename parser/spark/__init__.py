from .helper import SparkSqlHelper


def parse_string(sql, detail=False):
    return SparkSqlHelper.parse_string(sql, detail)


def parse_file(file, detail=False):
    return SparkSqlHelper.parse_file(file, detail)
