
from advent_of_code.core import data, map2d, mapt
from advent_of_code.point import *
_test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

test_input = data(_test_input, parser=lambda s: mapt(int, s))
_input = data('data/input9.txt', parser=lambda s: mapt(int, s), test=False)

print(test_input)

def count_lows(grid):
    m, n = len(grid), len(grid[0])
    lows = []
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            is_low = True
            for x,y in neighbors4((r, c)):
                if 0 <= x < m and 0 <= y < n:
                    is_low = is_low and val < grid[x][y]
            if is_low:
                lows.append(val)
    return lows

print(sum(low + 1 for low in count_lows(test_input)))
print(sum(low + 1 for low in count_lows(_input)))
