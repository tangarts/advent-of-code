from itertools import product
from collections import defaultdict
from advent_of_code.core import parse_input, integers

raw = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
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
        xyz.append((ranges[i], ranges[i+1]))
    return on_off, xyz
    
test = parse_input(raw, parser=parse)
_input = """on x=-30..22,y=-28..20,z=-17..37
on x=-20..34,y=-30..17,z=-30..21
on x=-7..42,y=-23..26,z=-18..29
on x=-8..44,y=-34..20,z=-14..32
on x=-13..32,y=-47..6,z=-38..6
on x=-48..6,y=-36..14,z=-18..33
on x=-31..13,y=-22..32,z=-44..9
on x=-18..31,y=-48..-2,z=-18..28
on x=-9..38,y=-15..35,z=-48..6
on x=-14..35,y=-42..6,z=-9..43
off x=25..40,y=-21..-12,z=3..18
on x=-32..12,y=-28..18,z=-12..40
off x=-12..1,y=27..38,z=5..18
on x=-34..14,y=-38..13,z=-29..23
off x=9..28,y=-35..-26,z=7..16
on x=-18..27,y=-21..27,z=-42..7
off x=18..32,y=26..42,z=-8..10
on x=-15..34,y=-30..17,z=-19..33
off x=12..23,y=32..45,z=26..41
on x=-36..13,y=-33..13,z=-27..17"""
test = parse_input(_input, parser=parse)

steps = [["on", (10, 12)], ["on", (11, 13)], ["off", (9, 11)], ["on", (10, 10)]]

def count_on(steps):
    cubes = defaultdict(int)
    for onoff, ranges in steps:
        x, y, z = ranges
        if onoff == "on":
            for cube in product(range(x[0], x[1] + 1), range(y[0], y[1] + 1), range(z[0], z[1] + 1)):
                cubes[cube] = 1
        elif onoff == "off":
            for cube in product(range(x[0], x[1] + 1), range(y[0], y[1] + 1), range(z[0], z[1] + 1)):
                cubes[cube] = 0

    return sum(cubes.values())


