import Math.Expression as ex


class Sum(ex.Expression):
    def __init__(self, top, bottom):
        """
        :param top: (Expression)
        :param bottom: (Expression)
        """
        super().__init__(ex.Type.SUM)
        self.top = top
        self.bottom = bottom

    def draw(self, handler):
        self.top.draw(handler)
        self.bottom.draw(handler)
        pass