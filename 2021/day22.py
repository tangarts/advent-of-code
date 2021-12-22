#%%
from itertools import count, product
from collections import defaultdict
from typing import Tuple
from advent_of_code.core import parse_input, integers

raw = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16"""

"""on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15"""


def parse(line):
    on_off, ranges = line.split(" ", maxsplit=1)
    xyz = []
    ranges = integers(ranges)
    for i in range(0, len(ranges), 2):
        xyz.append((ranges[i], ranges[i + 1]))
    return on_off, xyz


test = parse_input(raw, parser=parse)


##day22 = parse_input('data/input22.txt', parser=parse, test=False)


def count_on(steps):
    cubes = defaultdict(int)
    for onoff, ranges in steps:
        x, y, z = ranges
        if onoff == "on":
            for cube in product(
                range(x[0], x[1] + 1), range(y[0], y[1] + 1), range(z[0], z[1] + 1)
            ):
                cubes[cube] = 1
        elif onoff == "off":
            for cube in product(
                range(x[0], x[1] + 1), range(y[0], y[1] + 1), range(z[0], z[1] + 1)
            ):
                cubes[cube] = 0

    return sum(cubes.values())


count_on(test)

#%%


def overlap(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    l1, h1 = p1  # low and high points
    l2, h2 = p2

    # no overlap
    if max(l1, l2) > min(h1, h2):
        return 1
    return abs(min(h1, h2) - max(l1, l2)) + 1


#%%
intervals = {0: [0, 0], 1: [0, 0], 2: [0, 0]}  # x  # y  # z
total = 0
prod = 1
overlapping = 1
for j, (onoff, ranges) in enumerate(test):
    # x, y and z
    for i in range(3):
        overlapping *= overlap(intervals[i], ranges[i])
        prod *= len(range(*ranges[i])) + 1
        intervals[i][0] = min(intervals[i][0], ranges[i][0])
        intervals[i][1] = max(intervals[i][1], ranges[i][1])
    print(overlapping)
    print(intervals)
    total += prod
    # remove overlap
    if overlapping > 1:
        total -= overlapping
    prod = 1
    overlapping = 1


print(total)


# %%
# answer 210918
# 225476

# %%
def irange(start, stop):
    return range(start, stop + 1)


# %%
intervals
# %%
