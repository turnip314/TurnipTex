import math


class Type:
    NUMBER = 1
    BINARY_OP = 2


class Expression:
    def __init__(self, expr_type):
        self.TYPE = expr_type

    def __str__(self):
        raise Exception("__str__ not implemented for {}}".format(self.TYPE))

    def eval(self):
        raise Exception("eval not implemented for {}}".format(self.TYPE))


