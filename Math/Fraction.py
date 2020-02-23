import Math.Expression as ex
import Handlers.LineComponent as l


class Fraction(ex.Expression):
    THICKNESS = 8
    TOP_SCALE = 0.8
    BOTTOM_SCALE = 0.8
    TOP_SHIFT = 0.5
    BOTTOM_SHIFT = 0.5
    HORIZONTAL_SPACING = 0.2

    def __init__(self, top, bottom):
        """
        :param top: (Expression)
        :param bottom: (Expression)
        """
        super().__init__(ex.Type.FRACTION)
        self.top = top
        self.bottom = bottom

    def set_scale(self, scale=1):
        self.scale = scale
        self.top.set_scale(scale * self.TOP_SCALE)
        self.bottom.set_scale(scale * self.BOTTOM_SCALE)

    @property
    def get_width(self):
        """
        Gets width of itself and all sub-expressions
        :param scale:
        :return:
        """
        return max(
            self.top.get_width,
            self.bottom.get_width
        )

    @property
    def get_height(self):
        """
        Gets height of itself and all subexpressions
        :param scale:
        :return:
        """
        return self.THICKNESS * self.scale + \
               self.top.get_height + \
               self.THICKNESS * self.TOP_SHIFT * self.scale + \
               self.bottom.get_height + \
               self.THICKNESS * self.BOTTOM_SHIFT * self.scale

    @property
    def get_height_below_origin(self):
        """
        Gets height of itself and bottom
        :param scale:
        :return:
        """
        return self.THICKNESS * scale + \
               self.bottom.get_height(scale * self.BOTTOM_SCALE) + \
               self.THICKNESS * self.BOTTOM_SHIFT * scale

    @property
    def get_height_of_main_component(self):
        """
        Gets height of itself assuming no subexpressions
        :param scale:
        :return:
        """
        return self.THICKNESS * self.scale

    def draw(self, handler):
        x, y = handler.get_current_offset
        handler.add_component_shape(
            l.LineComponent((x, y), self.THICKNESS * self.scale, self.get_width))

        top_x = x + self.get_width * 0.5 - self.top.get_width * 0.5
        top_y = y - self.top.get_height_below_origin - self.THICKNESS * self.TOP_SHIFT * self.scale
        handler.set_offset(top_x, top_y)
        self.top.draw(handler)

        bottom_x = x + self.get_width * 0.5 - self.bottom.get_width * 0.5
        bottom_y = y + self.THICKNESS * self.scale + self.THICKNESS * self.BOTTOM_SHIFT * self.scale + \
                   self.bottom.get_height_above_origin
        handler.set_offset(bottom_x, bottom_y)
        self.bottom.draw(handler)
