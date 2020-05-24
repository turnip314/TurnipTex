import Math.Expression as ex


class Sub(ex.Expression):
    def __init__(self, base, expression):
        """
        :type base: ex.Expression
        :type val: ex.Expression
        """
        super().__init__(ex.Type.POWER)
        self.base = base
        self.expression = expression

    @property
    def is_center_align(self):
        return False

    @property
    def is_top_align(self):
        return True

    def set_scale(self, scale=1):
        self.scale = scale
        self.base.set_scale(scale)
        self.expression.set_scale(0.3 * scale)

    def initialize(self):
        self.base.initialize()
        self.expression.initialize()
        super().initialize()

    # BELOW ARE ALL TODO
    def initialize_width(self):
        self.width = self.base.get_width + self.expression.get_width

    def initialize_height(self):
        self.height = self.base.get_height + self.expression.get_height/2

    def initialize_height_below_origin(self):
        self.height_below_origin = self.base.get_height + self.expression.get_height/2

    def initialize_height_of_main_component(self):
        self.height_of_main_component = self.base.get_height

    def draw(self, handler):
        x, y = handler.get_current_offset
        self.base.draw(handler)
        y += self.base.get_height - self.expression.get_height / 2
        x += self.base.get_width
        handler.set_offset(x, y)
        self.expression.draw(handler)
