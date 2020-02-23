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
\\sum{n=1}{a \infty} - \\frac{1}{12}
"""

my_input = str(input())


handler = TexDrawHandler(my_input)
handler.draw()
