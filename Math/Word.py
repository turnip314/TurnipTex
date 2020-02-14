import Math.Expression as ex


class Word(ex.Expression):
    def __init__(self, texts):
        """
        :param text: (List[Text])
        """
        super().__init__(ex.Type.WORD)
        self.texts = texts

    def draw(self, handler):
        for text in self.texts:
            text.draw(handler)