import Math.Expression as ex


class Fraction(ex.Expression):
    TOP_SHIFT = 0

    def __init__(self, top, bottom):
        """
        :param top: (Expression)
        :param bottom: (Expression)
        """
        super().__init__(ex.Type.FRACTION)
        self.top = top
        self.bottom = bottom

    def draw(self, handler):
        self.top.draw(handler)
        self.bottom.draw(handler)
        pass