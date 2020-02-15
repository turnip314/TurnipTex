class Type:
    EXPR = "expr"
    TEXT = "text"
    WORD = "word"
    FRACTION = "frac"
    SUM = "sum"
    POWER = "pow"
    SUB = "sub"


class Expression:
    def __init__(self, expr_type):
        self.TYPE = expr_type

    def __str__(self):
        raise Exception("__str__ not implemented for {}}".format(self.TYPE))

    def draw(self, handler):
        raise Exception("Cannot draw abstract expression")
        pass


