import Math.Expression as ex
import Handlers.ImageComponent as img
import Handlers.TextComponent as txt


class Infinity(ex.Expression):
    IMAGE = "infty.png"
    WIDTH = 102
    HEIGHT = 90

    def __init__(self):
        """
        :param text: (string)
        """
        super().__init__(ex.Type.TEXT)

    def set_scale(self, scale=1):
        self.scale = scale

    def initialize_width(self):
        self.width = self.WIDTH * self.scale

    def initialize_height(self):
        self.height = self.HEIGHT * self.scale

    def initialize_height_below_origin(self):
        self.height_below_origin = self.get_height

    def initialize_height_of_main_component(self):
        self.height_of_main_component = self.get_height

    def draw(self, handler):
        handler.add_component_image(
            img.ImageComponent(self.IMAGE, handler.get_current_offset, self.scale)
        )
