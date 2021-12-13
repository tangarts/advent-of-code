from typing import Tuple
from advent_of_code.core import mapt, parse_input

raw_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


def to_point(points):
    points = points.splitlines()
    points = mapt(lambda p: mapt(int, p.split(",")), points)
    return points


def to_instruction(dirs: str):
    direction = [s.strip("fold along ") for s in dirs.splitlines()]
    direction = mapt(lambda s: s.split("="), direction)
    return direction


def points_and_instructions(data: list):
    points, instructions = data[0], data[1]
    points, instructions = to_point(points), to_instruction(instructions)
    return points, instructions


test_points, test_instructions = points_and_instructions(parse_input(raw_input, sep="\n\n"))

# let l be line number and n be fold line then
# after the fold the l coord becomes -l % n


set((x, y % 7) if y < 7 else (x, -y % 7) for x, y in test_points)

day13 = parse_input('data/input13.txt', sep="\n\n", test=False)
points, instructions = points_and_instructions(day13)


def fold_paper(points, line):
    direction, size = line
    size = int(size)
    if direction == 'y':
        return set((x, y % size)
                   if y < size else (x, -y % size)
                   for x, y in points)
    else:
        return set((x % size, y)
                   if x < size else (-x % size, y)
                   for x, y in points)


assert len(fold_paper(points, instructions[0])) == 763


### Part 2


for i in test_instructions:
    test_points = fold_paper(test_points, i)

end = "\n".join([''.join(["#" if (x, y) in test_points else "." for x in range(5)]) for y in range(5)])



for i in instructions:
    points = fold_paper(points, i)

max_x = max(points, key=lambda x: x[0])[0]
max_y = max(points, key=lambda y: y[1])[1]

out = "\n".join([''.join(["#" if (x, y) in test_points else "." for x in range(max_x)]) for y in range(max_y+1)])

print(out)
