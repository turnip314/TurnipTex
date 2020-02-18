import Math.Expression as ex
import Handlers.ImageComponent as img
import Handlers.TextComponent as txt


class Sum(ex.Expression):
    HEIGHT = 134
    WIDTH = 140
    IMAGE = 'sum.png'
    WIDTH_TO_HEIGHT = 1  # might need to adjust
    TOP_SCALE = 0.6
    BOTTOM_SCALE = 0.6
    TOP_SHIFT = -0.1
    BOTTOM_SHIFT = 0
    HORIZONTAL_SPACING = 0.2

    def __init__(self, bottom, top):
        """
        :param top: (Expression)
        :param bottom: (Expression)
        """
        super().__init__(ex.Type.SUM)
        self.bottom = bottom
        self.top = top

    def get_width(self, scale):
        """
        Gets width of itself and all sub-expressions
        :param scale:
        :return:
        """
        return max(
            self.top.get_width(scale * self.TOP_SCALE),
            self.bottom.get_width(scale * self.BOTTOM_SCALE),
            self.WIDTH * scale
        )

    def get_height(self, scale):
        """
        Gets height of itself and all subexpressions
        :param scale:
        :return:
        """
        return self.HEIGHT * scale + \
               self.top.get_height(scale * self.TOP_SCALE) + \
               self.HEIGHT * self.TOP_SHIFT * scale + \
               self.bottom.get_height(scale * self.BOTTOM_SCALE) + \
               self.HEIGHT * self.BOTTOM_SHIFT * scale

    def get_height_from_origin(self, scale):
        """
        Gets height of itself and bottom
        :param scale:
        :return:
        """
        return self.HEIGHT * scale + \
               self.bottom.get_height(scale * self.BOTTOM_SCALE) + \
               self.HEIGHT * self.BOTTOM_SHIFT * scale

    def draw(self, handler, scale=1):
        x, y = handler.get_current_offset
        handler.add_component_image(img.ImageComponent(self.IMAGE, (x, y), scale))

        top_x = x + self.WIDTH * scale * 0.5 - self.top.get_width(scale * self.TOP_SCALE) * 0.5
        top_y = y - self.top.get_height_from_origin(scale * self.TOP_SCALE) + self.HEIGHT * self.TOP_SHIFT * scale
        handler.set_offset(top_x, top_y)
        self.top.draw(handler, scale * self.TOP_SCALE)

        bottom_x = x + self.WIDTH * scale * 0.5 - self.bottom.get_width(scale * self.BOTTOM_SCALE) * 0.5
        bottom_y = y + self.HEIGHT * scale + self.HEIGHT * self.BOTTOM_SHIFT * scale
        handler.set_offset(bottom_x, bottom_y)
        self.bottom.draw(handler, scale * self.BOTTOM_SCALE)
