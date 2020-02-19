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

    def get_height(self, scale):
        raise Exception("Height not implemented")

    def get_height_below_origin(self, scale):
        raise Exception("Height from origin not implemented")

    def get_height_above_origin(self, scale):
        return self.get_height(scale) - self.get_height_below_origin(scale)

    def get_height_of_main_component(self, scale):
        raise Exception("Height of main component not implemented")

    def draw(self, handler):
        raise Exception("Cannot draw abstract expression")
        pass


