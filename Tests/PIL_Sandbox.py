from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGBA', (1440, 900), (255, 0, 0, 0))

sum = Image.open("../Resources/sum.png").convert('RGBA')
image.paste(sum, (0, 0))

# get a font
fnt = ImageFont.truetype('../Resources/cmu/cmunbi.ttf', 140)

draw = ImageDraw.Draw(image)
draw.text((0,0), "x1l|", font=fnt)

image.save("image.png", "PNG")
