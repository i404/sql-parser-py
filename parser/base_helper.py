from io import TextIOWrapper


class BaseHelper:
    @staticmethod
    def parse_string(sql: str, detail):
        raise Exception("")

    @classmethod
    def parse_file(cls, file, detail=False):
        if isinstance(file, str):
            with open(file, 'r') as f:
                return cls.parse_string(f.read(), detail)
        elif isinstance(file, TextIOWrapper):
            return cls.parse_string(file.read(), detail)
