import Math.Expression as ex


class Power(ex.Expression):
    def __init__(self, val):
        """
        :param val: (Expression)
        """
        super().__init__(ex.Type.POWER)
        self.val = val

    def draw(self, handler):
        pass