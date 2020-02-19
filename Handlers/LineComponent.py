from PIL import Image, ImageDraw, ImageFont


class LineComponent:
    def __init__(self, left, width, length):
        self.left = left
        self.width = width
        self.length = length

    @property
    def get_x(self):
        return self.left[0]

    @property
    def get_y(self):
        return self.left[1]

    def shift_by(self, x, y):
        self.left = (self.left[0] + x, self.left[1] + y)

    def draw(self, draw):
        draw.line([self.left, (self.left[0] + self.length, self.left[1])], fill="black", width=int(self.width) or 1)
