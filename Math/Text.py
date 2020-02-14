import Math.Expression as ex


class Text(ex.Expression):
    def __init__(self, text):
        """
        :param text: (string)
        """
        super().__init__(ex.Type.TEXT)
        self.text = text

    def draw(self, handler):
        pass