from PIL import Image, ImageDraw, ImageFont, ImageColor


class TextComponent:
    DEFAULT_SIZE = 100

    def __init__(self, text, top_left, scale, font='cmunbi.ttf'):
        self.text = text
        self.top_left = top_left
        self.scale = scale
        self.font = ImageFont.truetype('../Resources/cmu/' + font, int(100*scale))

    @property
    def get_x(self):
        return self.top_left[0]

    @property
    def get_y(self):
        return self.top_left[1]

    def shift_by(self, x, y):
        self.top_left = (self.top_left[0] + x, self.top_left[1] + y)

    @property
    def get_width(self):
        image = Image.new('RGBA', (1440, 900), (255, 0, 0, 0))

        sum = Image.open("../Resources/sum.png").convert('RGBA')

        draw = ImageDraw.Draw(image)
        return draw.textsize(self.text, font=self.font)[0]

    @property
    def get_height(self):
        image = Image.new('RGBA', (1440, 900), (255, 0, 0, 0))

        sum = Image.open("../Resources/sum.png").convert('RGBA')

        draw = ImageDraw.Draw(image)
        return draw.textsize("g", font=self.font)[1]

    def draw(self, draw):
        draw.text(self.top_left, self.text, fill="black", font=self.font)
