import math
from statistics import mean
from sys import getsizeof
from uuid import uuid4

import PIL.Image

MOVES = 13

first_array = []
second_array = []

# trick to create a memory ballast. After that memory can be written in a clear for computer science way.
clapper = [uuid4() for _ in range(MOVES**2)]

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

width = math.ceil(math.sqrt(shift))
height = width

image: PIL.Image.Image = PIL.Image.new('HSV', (width, height))

def draw(elements, ids, hue):
    for element, element_id in zip(elements, ids):
        for i in range(getsizeof(element)):
            x = (element_id + i) % width
            y = (element_id + i) // width
            p = image.getpixel((x, y))
            if p != (0, 0, 0):
                raise ValueError
            image.putpixel((x, y), (hue, 213, 255))

draw(first_array[:MOVES], first_ids[:MOVES], 0)
draw(first_array[MOVES:], first_ids[MOVES:], 10)
draw(second_array, second_ids, 90)

image.show()
image.convert("RGB").resize((480, 480), PIL.Image.NEAREST).save(f"demo{MOVES}.png")
