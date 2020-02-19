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

    def get_height_below_origin(self, scale):
        return max([expr.get_height_below_origin(scale) for expr in self.expressions])

    def draw(self, handler, scale=1):
        x, y = handler.get_current_offset
        max_component_height = max([expr.get_height_of_main_component(scale) for expr in self.expressions])
        for expr in self.expressions:
            component_height = expr.get_height_of_main_component(scale)
            cur_y = y + max_component_height/2.0 - component_height/2.0
            handler.set_offset(x, cur_y)
            expr.draw(handler, scale)
            x += expr.get_width(scale)
