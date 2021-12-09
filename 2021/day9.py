#%%
from math import prod
from collections import deque
from advent_of_code.core import data, mapt
from advent_of_code.point import neighbors4

_test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

test_input = data(_test_input, parser=lambda s: list(map(int, s)))
_input = data("data/input9.txt", parser=lambda s: list(map(int, s)), test=False)


def count_lows(grid):
    m, n = len(grid), len(grid[0])
    lows = []
    q = deque([])
    basins = {}
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            is_low = True

            for x, y in neighbors4((r, c)):
                if 0 <= x < m and 0 <= y < n:
                    is_low = is_low and val < grid[x][y]
            if is_low:
                lows.append(val)
                q.append((r, c))
                basins[(r, c)] = 0

                while q:
                    curr = q.popleft()
                    count = 0
                    for x, y in neighbors4(curr):
                        # OOB
                        if (
                            0 <= x < m
                            and 0 <= y < n
                            and grid[x][y] != 9
                            and grid[x][y] != -1
                        ):
                            basins[(r, c)] += 1
                            grid[x][y] = -1
                            q.append((x, y))

    return prod(sorted(basins.values())[-3:])


count_lows(_input)
# print(sum(low + 1 for low in count_lows(test_input)))
# print(sum(low + 1 for low in count_lows(_input)))
