from PIL import Image, ImageDraw, ImageFont


class ImageComponent:
    def __init__(self, src_img, top_left, scale):
        self.src_img = '../Resources/' + src_img
        self.top_left = top_left
        self.scale = scale

    @property
    def get_x(self):
        return self.top_left[0]

    @property
    def get_y(self):
        return self.top_left[1]

    def shift_by(self, x, y):
        self.top_left = (self.top_left[0] + x, self.top_left[1] + y)

    def draw(self, image):
        image_component = Image.open(self.src_img).convert('RGBA')
        width, height = image_component.size
        new_size = (int(width * self.scale), int(height * self.scale))
        image_component = image_component.resize(new_size, Image.ANTIALIAS)
        image.paste(image_component, (int(self.top_left[0]), int(self.top_left[1])))
