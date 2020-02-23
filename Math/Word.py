import Math.Expression as ex

class Word(ex.Expression):
    def __init__(self, texts):
        """
        :param text: (List[Text])
        """
        super().__init__(ex.Type.WORD)
        self.texts = texts

    def set_scale(self, scale=1):
        self.scale = scale
        for text in self.texts:
            text.set_scale(scale)

    @property
    def get_width(self):
        return sum([text.get_width for text in self.texts])

    @property
    def get_height(self):
        return max([text.get_height for text in self.texts])

    @property
    def get_height_of_main_component(self):
        return self.get_height

    @property
    def get_height_below_origin(self):
        return self.get_height

    def draw(self, handler):
        x, y = handler.get_current_offset
        for text in self.texts:
            text.draw(handler)
            x += text.get_width
            handler.set_offset(x, y)
