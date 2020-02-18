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

    def get_width(self, scale):
        return txt.TextComponent(self.text, (0,0), scale).get_width

    def get_height(self, scale):
        return txt.TextComponent(self.text, (0,0), scale).get_height

    def draw(self, handler, scale=1):
        handler.add_component_text(
            txt.TextComponent(self.text, handler.get_current_offset, scale)
        )
