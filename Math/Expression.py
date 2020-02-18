class Type:
    EXPR = "expr"
    TEXT = "text"
    WORD = "word"
    FRACTION = "frac"
    SUM = "sum"
    POWER = "pow"
    SUB = "sub"


class AXIS:
    VERTICAL = 1
    HORIZONTAL = 2


class RESTRICTION:
    TOP = 1
    BOTTOM = 2
    LEFT = 3


class Expression:
    def __init__(self, expr_type):
        self.TYPE = expr_type

    def __str__(self):
        raise Exception("__str__ not implemented for {}}".format(self.TYPE))

    def draw(self, handler):
        raise Exception("Cannot draw abstract expression")
        pass


