from collections import deque
from typing import Tuple, List
from advent_of_code.core import data, repeat, repeatedly
from advent_of_code.point import neighbors8


# looks like a BFS to me

test11 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

test_data11 = data(test11, parser=lambda s: list(map(int,s)))


def step(stuff) -> Tuple[List[List[int]], int]:
    grid, flashes = stuff
   
    def flash(grid, r, c, seen=set()):
        m, n = len(grid), len(grid[0])
        # base, already flashed
        if grid[r][c] == 0 and (r, c) in seen:
            return 
        # First, the level of each octopus increases by 1
        grid[r][c] += 1

        # flash if current square is greater than 9
        if grid[r][c] > 9:
            grid[r][c] = 0  # flashed and set to zero
            seen.add((r,c)) # and seen
            # check neighbours
            for x, y in neighbors8((r, c)):
                if 0 <= x < m and 0 <= y < n and (x,y) not in seen:
                    flash(grid, x, y, seen)
        return 

    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            flash(grid, r, c)

    flashes += sum(1 for x in range(len(grid))
                     for y in range(len(grid[0])) 
                     if grid[x][y] == 0)

    return grid, flashes

# print(repeat(100, step, (test_data11, 0))) # 1656

day11 = data('data/input11.txt', parser=lambda s: list(map(int,s)), test=False)
# print(repeat(100, step, (day11, 0))) # 1673

def part2(stuff: Tuple[List[List[int]], int]) -> int:
    iteration = 0
    while True:
        grid, flashes = step(stuff)
        iteration += 1
        if flashes == 100:
            break
        else:
            stuff = grid, 0
    return iteration

print(part2((test_data11, 0)))
print(part2((day11, 0))) ##

    
