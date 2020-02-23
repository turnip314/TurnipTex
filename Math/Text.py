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

    @property
    def get_width(self):
        return txt.TextComponent(self.text, (0,0), self.scale).get_width + self.scale * 10

    @property
    def get_height(self):
        return txt.TextComponent(self.text, (0,0), self.scale).get_height

    def draw(self, handler):
        handler.add_component_text(
            txt.TextComponent(self.text, handler.get_current_offset, self.scale)
        )
