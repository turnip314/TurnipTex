import Math.Expression as ex

class Word(ex.Expression):
    def __init__(self, texts):
        """
        :param text: (List[Text])
        """
        super().__init__(ex.Type.WORD)
        self.texts = texts

    def initialize(self):
        for text in self.texts:
            text.initialize()
        super().initialize()

    def set_scale(self, scale=1):
        self.scale = scale
        for text in self.texts:
            text.set_scale(scale)

    def initialize_width(self):
        self.width = sum([text.get_width for text in self.texts])

    def initialize_height(self):
        self.height = max([text.get_height for text in self.texts])

    def initialize_height_below_origin(self):
        self.height_below_origin = self.get_height

    def initialize_height_of_main_component(self):
        self.height_of_main_component = self.get_height

    def draw(self, handler):
        x, y = handler.get_current_offset
        for text in self.texts:
            text.draw(handler)
            x += text.get_width
            handler.set_offset(x, y)
