from dataclasses import dataclass
import numpy as np
from typing import Tuple
from typing import List
maps = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split('\n')

with open("17.txt", 'r') as file:
    lines = [i.rstrip() for i in file.readlines()]

print(lines)

@dataclass
class Stone:
    coordinates: Tuple[int,int]
    
@dataclass
class Rock:
    stones: List[Stone]

@dataclass
class Bottom:
    stones: List[List[Stone]]

    def get_heighest_x_pos(self):
        highest = 0
        x = 0
        for index, i in enumerate(self.stones):
            if len(i) > highest:
                highest = len(i)
                x = index
        return highest


class Field:
    def __init__(self, bottom: Bottom, rock: Rock) -> None:
        # Set offset to x
        new_x_rock = Rock([])
        sorted_x = sorted(rock.stones, key=lambda stone: stone.coordinates[0])
        for index_x, stone in enumerate(sorted_x):
            new_x_rock.stones.append(Stone((2 + index_x, stone.coordinates[1])))
        print_rock(new_x_rock)

        # Set height
        y_rock = Rock([])
        sorted_y = sorted(new_x_rock.stones, key=lambda stone: stone.coordinates[1])
        highest = bottom.get_heighest_x_pos()
        new_y_rock = list(map(lambda stone: Stone((stone.coordinates[0], stone.coordinates[1] + highest + 2)), sorted_y))
        self.bottom = bottom
        y_rock.stones.extend(new_y_rock)
        self.rock = y_rock

        print("Made field")
        print_rock(self.rock)

        

# Set up Bottom

bottom = Bottom([])
for i in range(7):
    bottom.stones.append([Stone((i,0))])

# Read in Rocks

rocks = []
rock = Rock([])
index_y = 0
for line in maps:
    if line == '':
        rocks.append(rock)
        rock = Rock([])
        index_y = 0
        continue

    for index_x, x_char in enumerate(line):
        if x_char == '#':
            rock.stones.append(Stone((index_x, index_y)))

    index_y += 1

rocks.append(rock)

def print_rock(rock: Rock):
    print("======================")
    matrix = np.zeros((7,7), dtype=int)
    for stone in rock.stones:
        matrix[stone.coordinates[1],stone.coordinates[0]] = 1
    print(matrix)
    print("======================")


def print_rocks(rocks: List[Rock]):
    for rock in rocks:
        print_rock(rock)

for instruction in lines:
    print(instruction)
    for rock in rocks:
        field = Field(bottom, rock)
