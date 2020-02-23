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
        self.scale = 1

    def __str__(self):
        raise Exception("__str__ not implemented for {}}".format(self.TYPE))

    def set_scale(self, scale=1):
        raise Exception("Scale not implemented")

    @property
    def get_height(self):
        raise Exception("Height not implemented")

    @property
    def get_height_below_origin(self):
        raise Exception("Height from origin not implemented")

    @property
    def get_height_above_origin(self):
        return self.get_height - self.get_height_below_origin

    @property
    def get_height_of_main_component(self):
        raise Exception("Height of main component not implemented")

    def draw(self, handler):
        raise Exception("Cannot draw abstract expression")
        pass


