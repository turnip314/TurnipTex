class Type:
    TEXT = 1
    WORD = 2
    FRACTION = 3
    SUM = 4

class Expression:
    def __init__(self, expr_type):
        self.TYPE = expr_type

    def __str__(self):
        raise Exception("__str__ not implemented for {}}".format(self.TYPE))

    def draw(self, handler):
        raise Exception("Cannot draw abstract expression")
        pass


