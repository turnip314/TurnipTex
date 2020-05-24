import Math.Expression as ex
import Handlers.ImageComponent as img


class Paren(ex.Expression):
    LP = "lp.png"
    RP = "rp.png"

    def __init__(self, expression):
        """
        :param val: (Expression)
        """
        super().__init__(ex.Type.EXPR)
        self.expression = expression
        self.adjusted_scale = None

    def set_scale(self, scale=1):
        self.scale = scale
        self.expression.set_scale(scale)

    def initialize(self):
        self.expression.initialize()
        self.adjusted_scale = self.expression.get_height / 80.0
        super().initialize()

    # BELOW ARE ALL TODO
    def initialize_width(self):
        self.width = 2 * 24 * self.adjusted_scale + self.expression.get_width

    def initialize_height(self):
        self.height = self.expression.get_height

    def initialize_height_below_origin(self):
        self.height_below_origin = self.height

    def initialize_height_of_main_component(self):
        self.height_of_main_component = self.height

    def draw(self, handler):
        x, y = handler.get_current_offset
        handler.add_component_image(img.ImageComponent(self.LP, (x, y), self.adjusted_scale))
        handler.set_offset(x + 24 * self.adjusted_scale, y + self.expression.get_height_above_origin)
        self.expression.draw(handler)
        handler.add_component_image(img.ImageComponent(self.RP, (x + self.expression.width + 24*self.adjusted_scale, y), self.adjusted_scale))
