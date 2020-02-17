import Math.Expression as ex


class Sum(ex.Expression):
    TOP_SCALE = 0.16
    BOTTOM_SCALE = 0.16
    TOP_SHIFT = 0
    MAIN_SHIFT = 0.25
    BOTTOM_SHIFT = 0.84
    HORIZONTAL_SPACING = 0.2

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