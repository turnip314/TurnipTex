import Math.Expression as ex


class Sub(ex.Expression):
    def __init__(self, val):
        """
        :param val: (Expression)
        """
        super().__init__(ex.Type.SUB)
        self.val = val

    def draw(self, handler):
        pass