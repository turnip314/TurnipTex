from PIL import Image, ImageDraw


class TexDrawHandler:
    def __init__(self, input_string):
        self.input_string = input_string
        self._components = []
        self.offset = (0,0)
        self.texts = []
        self.images = []

    def add_component_text(self, component):
        self._components.append(component)
        self.texts.append(component)

    def add_component_image(self, component):
        self._components.append(component)
        self.images.append(component)

    @property
    def get_current_offset(self):
        return self.offset

    def set_offset(self, x, y):
        self.offset = (x, y)

    def draw(self, destination="result.png"):
        min_x = min([component.get_x for component in self._components])
        min_y = min([component.get_y for component in self._components])
        for component in self._components:
            component.shift_by(-min_x, -min_y)

        image = Image.new('RGBA', (500, 500), (255, 0, 0, 0))
        for image_component in self.images:
            image_component.draw(image)

        draw = ImageDraw.Draw(image)
        for text_component in self.texts:
            text_component.draw(draw)

        image.save(destination, "PNG")
