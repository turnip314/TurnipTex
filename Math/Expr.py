import Math.Expression as ex


class Expr(ex.Expression):
    def __init__(self, expressions):
        """
        :param val: (Expression)
        """
        super().__init__(ex.Type.EXPR)
        self.expressions = expressions

    def get_width(self, scale):
        return sum([expr.get_width(scale) for expr in self.expressions])

    def get_height(self, scale):
        return max([expr.get_height(scale) for expr in self.expressions])

    def get_height_from_origin(self, scale):
        return max([expr.get_height_from_origin(scale) for expr in self.expressions])

    def draw(self, handler, scale=1):
        for expr in self.expressions:
            expr.draw(handler, scale)
