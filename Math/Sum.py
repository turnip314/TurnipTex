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
    TOP_SHIFT = 0.05
    BOTTOM_SHIFT = 0.05
    HORIZONTAL_SPACING = 0.2

    def __init__(self, bottom, top):
        """
        :param top: (Expression)
        :param bottom: (Expression)
        """
        super().__init__(ex.Type.SUM)
        self.bottom = bottom
        self.top = top

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
            self.bottom.get_width,
            self.WIDTH * self.scale
        )

    @property
    def get_height(self):
        """
        Gets height of itself and all subexpressions
        :param scale:
        :return:
        """
        return self.HEIGHT * self.scale + \
               self.top.get_height + \
               self.HEIGHT * self.TOP_SHIFT * self.scale + \
               self.bottom.get_height + \
               self.HEIGHT * self.BOTTOM_SHIFT * self.scale

    @property
    def get_height_below_origin(self):
        """
        Gets height of itself and bottom
        :param scale:
        :return:
        """
        return self.HEIGHT * self.scale + \
               self.bottom.get_height + \
               self.HEIGHT * self.BOTTOM_SHIFT * self.scale

    @property
    def get_height_of_main_component(self):
        """
        Gets height of itself assuming no subexpressions
        :param scale:
        :return:
        """
        return self.HEIGHT * self.scale

    def draw(self, handler):
        x, y = handler.get_current_offset
        handler.add_component_image(img.ImageComponent(self.IMAGE, (x, y), self.scale))

        top_x = x + self.WIDTH * self.scale * 0.5 - self.top.get_width * 0.5
        top_y = y - self.top.get_height_below_origin - self.HEIGHT * self.TOP_SHIFT * self.scale
        handler.set_offset(top_x, top_y)
        self.top.draw(handler)

        bottom_x = x + self.WIDTH * self.scale * 0.5 - self.bottom.get_width * 0.5
        bottom_y = y + self.HEIGHT * self.scale + self.HEIGHT * self.BOTTOM_SHIFT * self.scale + \
                   self.bottom.get_height_above_origin
        handler.set_offset(bottom_x, bottom_y)
        self.bottom.draw(handler)
