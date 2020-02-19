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

    def get_width(self, scale):
        """
        Gets width of itself and all sub-expressions
        :param scale:
        :return:
        """
        return max(
            self.top.get_width(scale * self.TOP_SCALE),
            self.bottom.get_width(scale * self.BOTTOM_SCALE)
        )

    def get_height(self, scale):
        """
        Gets height of itself and all subexpressions
        :param scale:
        :return:
        """
        return self.THICKNESS * scale + \
               self.top.get_height(scale * self.TOP_SCALE) + \
               self.THICKNESS * self.TOP_SHIFT * scale + \
               self.bottom.get_height(scale * self.BOTTOM_SCALE) + \
               self.THICKNESS * self.BOTTOM_SHIFT * scale

    def get_height_below_origin(self, scale):
        """
        Gets height of itself and bottom
        :param scale:
        :return:
        """
        return self.THICKNESS * scale + \
               self.bottom.get_height(scale * self.BOTTOM_SCALE) + \
               self.THICKNESS * self.BOTTOM_SHIFT * scale

    def get_height_of_main_component(self, scale):
        """
        Gets height of itself assuming no subexpressions
        :param scale:
        :return:
        """
        return self.THICKNESS * scale

    def draw(self, handler, scale=1):
        x, y = handler.get_current_offset
        handler.add_component_shape(l.LineComponent((x,y), self.THICKNESS*scale, self.get_width(scale)))

        top_x = x + self.get_width(scale) * 0.5 - self.top.get_width(scale * self.TOP_SCALE) * 0.5
        top_y = y - self.top.get_height_below_origin(scale * self.TOP_SCALE) - self.THICKNESS * self.TOP_SHIFT * scale
        handler.set_offset(top_x, top_y)
        self.top.draw(handler, scale * self.TOP_SCALE)

        bottom_x = x + self.get_width(scale) * 0.5 - self.bottom.get_width(scale * self.BOTTOM_SCALE) * 0.5
        bottom_y = y + self.THICKNESS * scale + self.THICKNESS * self.BOTTOM_SHIFT * scale + self.bottom.get_height_above_origin(scale * self.BOTTOM_SCALE)
        handler.set_offset(bottom_x, bottom_y)
        self.bottom.draw(handler, scale * self.BOTTOM_SCALE)