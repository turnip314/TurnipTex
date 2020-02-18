from PIL import Image, ImageDraw, ImageFont
from Handlers.TextDrawHandler import *
from Parsing.Tex.TexExpressionTreeGenerator import *

image = Image.new('RGBA', (1440, 900), (255, 0, 0, 0))

sum = Image.open("../Resources/sum.png").convert('RGBA')
image.paste(sum, (0, 0))

# get a font
fnt = ImageFont.truetype('../Resources/cmu/cmunbi.ttf', 140)

draw = ImageDraw.Draw(image)
draw.text((0,0), "g", font=fnt)

image.save("image.png", "PNG")

my_input = """
\\sum{a}{\\sum{b}{c}}
"""

generator = TexExpressionTreeGenerator()
result = generator.generate_expression_from_input(my_input)
handler = TexDrawHandler("")
result.draw(handler)
handler.draw()