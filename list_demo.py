import math
from statistics import mean
from sys import getsizeof
from uuid import uuid4
import colors

import PIL.Image

MOVES = 2

first_array = []
second_array = []

# trick to create a memory ballast. After that memory can be written in a clear for computer science way.
clapper = [uuid4() for _ in range((max(MOVES, 90))**2)]

for _ in range(MOVES):
    first_array.append(uuid4())

for _ in range(MOVES):
    second_array.append(uuid4())

for _ in range(MOVES):
    first_array.append(uuid4())

first_ids = []
for i in first_array:
    first_ids.append(id(i))

second_ids = []
for i in second_array:
    second_ids.append(id(i))


zero = min([*first_ids, *second_ids])
limit = max([*first_ids, *second_ids])
shift = limit - zero + getsizeof(uuid4())

for index, object_id in enumerate(first_ids):
    first_ids[index] = (object_id - zero)

for index, object_id in enumerate(second_ids):
    second_ids[index] = (object_id - zero)


side = math.sqrt(shift)
width = math.ceil(side * 1.4)
height = math.ceil(side / 1.4)

image: PIL.Image.Image = PIL.Image.new('RGB', (width, height))

def draw(elements, ids, color):
    for element, element_id in zip(elements, ids):
        for i in range(getsizeof(element)):
            x = (element_id + i) % width
            y = (element_id + i) // width
            p = image.getpixel((x, y))
            if p != (0, 0, 0):
                raise ValueError
            image.putpixel((x, y), color)

draw(first_array[:MOVES], first_ids[:MOVES], colors.MAXIMUM_RED)
draw(first_array[MOVES:], first_ids[MOVES:], colors.MAXIMUM_RED)
draw(second_array, second_ids, colors.CARROT_ORANGE)

# image.show()
image.resize((math.ceil(480 * 1.4), math.ceil(480 / 1.4)), PIL.Image.NEAREST).save(f"demo{MOVES}.png")