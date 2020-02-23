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

    @property
    def get_width(self):
        return self.WIDTH * self.scale

    @property
    def get_height_of_main_component(self):
        return self.get_height

    @property
    def get_height_below_origin(self):
        return self.get_height

    @property
    def get_height(self):
        return self.HEIGHT * self.scale

    def draw(self, handler, scale=1):
        handler.add_component_image(
            img.ImageComponent(self.IMAGE, handler.get_current_offset, scale)
        )
