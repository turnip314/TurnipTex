import Math.Expression as ex


class Paren(ex.Expression):
    def __init__(self, expression):
        """
        :param val: (Expression)
        """
        super().__init__(ex.Type.EXPR)
        self.expression = expression

    def set_scale(self, scale=1):
        self.scale = scale
        self.expression.set_scale(scale)

    def initialize(self):
        self.expression.initialize()
        super().initialize()

    # BELOW ARE ALL TODO
    def initialize_width(self):
        self.width = self.expression.get_width

    def initialize_height(self):
        self.height = self.expression.get_height

    def initialize_height_below_origin(self):
        self.height_below_origin = self.height

    def initialize_height_of_main_component(self):
        self.height_of_main_component = self.height

    def draw(self, handler):
        self.expression.draw(handler)
