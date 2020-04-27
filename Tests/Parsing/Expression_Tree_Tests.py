from PIL import Image, ImageDraw, ImageFont
from Handlers.TextDrawHandler import *
from Parsing.Tex.TexExpressionTreeGenerator import *

my_input = """
(\\frac{a_1}{2^{\\frac{1}{2}}})
"""

generator = TexExpressionTreeGenerator()
result = generator.generate_expression_from_input(my_input)
1
1
print(result)
