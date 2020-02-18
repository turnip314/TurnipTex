import Math.Expression as ex

class Word(ex.Expression):
    def __init__(self, texts):
        """
        :param text: (List[Text])
        """
        super().__init__(ex.Type.WORD)
        self.texts = texts

    def get_width(self, scale):
        return sum([text.get_width(scale) for text in self.texts])

    def get_height(self, scale):
        return max([text.get_height(scale) for text in self.texts])

    def get_height_from_origin(self, scale):
        return self.get_height(scale)

    def draw(self, handler, scale=1):
        x, y = handler.get_current_offset
        for text in self.texts:
            text.draw(handler, scale)
            handler.set_offset(x + text.get_width(scale), y)
