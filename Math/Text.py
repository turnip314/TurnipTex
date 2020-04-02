import Math.Expression as ex
import Handlers.ImageComponent as img
import Handlers.TextComponent as txt


class Text(ex.Expression):
    def __init__(self, text):
        """
        :param text: (string)
        """
        super().__init__(ex.Type.TEXT)
        self.text = text

    def set_scale(self, scale=1):
        self.scale = scale

    def initialize_width(self):
        self.width = txt.TextComponent(self.text, (0,0), self.scale).get_width + self.scale * 10

    def initialize_height(self):
        self.height = txt.TextComponent(self.text, (0,0), self.scale).get_height

    def initialize_height_below_origin(self):
        self.height_below_origin = self.get_height

    def initialize_height_of_main_component(self):
        self.height_of_main_component = self.get_height

    def draw(self, handler):
        handler.add_component_text(
            txt.TextComponent(self.text, handler.get_current_offset, self.scale)
        )
