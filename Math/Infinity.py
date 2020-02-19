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

    def get_width(self, scale):
        return self.WIDTH * scale

    def get_height_of_main_component(self, scale):
        return self.get_height(scale)

    def get_height_below_origin(self, scale):
        return self.get_height(scale)

    def get_height(self, scale):
        return self.HEIGHT * scale

    def draw(self, handler, scale=1):
        handler.add_component_image(
            img.ImageComponent(self.IMAGE, handler.get_current_offset, scale)
        )
