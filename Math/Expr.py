import Math.Expression as ex


class Expr(ex.Expression):
    def __init__(self, expressions):
        """
        :param val: (Expression)
        """
        super().__init__(ex.Type.EXPR)
        self.expressions = expressions

    def set_scale(self, scale=1):
        self.scale = scale
        for expr in self.expressions:
            expr.set_scale(scale)

    @property
    def get_width(self):
        return sum([expr.get_width for expr in self.expressions])

    @property
    def get_height(self):
        """
        Height is calculated by
        Max Height of main component / 2 + height above main component (origin)
        Max Height of main component / 2 + height below main component (origin)
        :return:
        """
        return max(
                [expr.get_height_of_main_component/2 + expr.get_height_above_origin for expr in self.expressions]
            ) + max(
                [expr.get_height_below_origin - expr.get_height_of_main_component/2 for expr in self.expressions]
            )



    @property
    def get_height_below_origin(self):
        return max([expr.get_height_below_origin for expr in self.expressions])

    @property
    def get_height_of_main_component(self):
        return self.get_height

    def draw(self, handler):
        x, y = handler.get_current_offset
        max_component_height = max([expr.get_height_of_main_component for expr in self.expressions])
        for expr in self.expressions:
            component_height = expr.get_height_of_main_component
            cur_y = y + max_component_height/2.0 - component_height/2.0
            handler.set_offset(x, cur_y)
            expr.draw(handler)
            x += expr.get_width
