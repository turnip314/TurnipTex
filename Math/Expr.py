import Math.Expression as ex


class Expr(ex.Expression):
    def __init__(self, expressions):
        """
        :param val: (Expression)
        """
        super().__init__(ex.Type.EXPR)
        self.expressions = expressions

    def draw(self, handler):
        pass
