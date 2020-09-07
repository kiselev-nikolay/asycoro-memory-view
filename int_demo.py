import math
from statistics import mean
from sys import getsizeof
from uuid import uuid4
import colors

from PIL import Image, ImageFont, ImageDraw

# trick to create a memory ballast. After that memory can be written in a clear for computer science way.
clapper = [uuid4() for _ in range(90**2)]

scope = [
    0,
    1,
    2,
    10_000,
    (2**32),
    (2**64),
    (2**128),
    (2**(2**8)),
    (2**(2**9)),
    (2**(2**10)),
]


width = 165
height = len(scope) + 1

image: Image.Image = Image.new('RGB', (width, height))

def draw(elements, color):
    offset = 1
    for element in elements:
        for i in range(getsizeof(element)):
            x = i
            y = offset
            p = image.getpixel((x, y))
            if p != (0, 0, 0):
                raise ValueError
            image.putpixel((x, y), color)
        offset += 1

draw(scope, colors.MAXIMUM_RED)

image = image.resize((math.ceil(width * 16), math.ceil(height * 16)), Image.NEAREST)

font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", size=7)
paint = ImageDraw.ImageDraw(image)

for i in range(width):
    paint.text((4+(i*16), (16-7)/4), str(i), font=font, stroke_fill=colors.MAXIMUM_RED)
    paint.line([(i * 16, 0), (i * 16, height * 16)])

image.show()
# image.save(f"demo_int.png")
