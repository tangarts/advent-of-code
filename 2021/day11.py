from collections import deque
from typing import Callable, Tuple, List
from advent_of_code.core import parse_input, repeat, repeatedly
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

test_data11 = parse_input(test11, parser=lambda s: list(map(int, s)))


def recursive_step(stuff) -> Tuple[List[List[int]], int]:
    grid, flashes = stuff

    def dfs(grid, r, c, seen=set()):
        m, n = len(grid), len(grid[0])
        # base, already flashed
        if (r, c) in seen:
            return
        # First, the level of each octopus increases by 1
        grid[r][c] += 1

        # flash if current square is greater than 9
        if grid[r][c] > 9:
            grid[r][c] = 0  # flashed and set to zero
            seen.add((r, c))  # and seen
            # check neighbours
            for x, y in neighbors8((r, c)):
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    dfs(grid, x, y, seen)
        return

    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            dfs(grid, r, c)

    flashes += sum(1 for x in range(len(grid))
                   for y in range(len(grid[0]))
                   if grid[x][y] == 0)

    return grid, flashes


def iterative_step(stuff):

    grid, flashes = stuff
    m, n = len(grid), len(grid[0])
    seen = set()
    q = deque([])
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            grid[r][c] += 1
            if grid[r][c] > 9:
                q.append((r, c))
                seen.add((r, c))
    while q:
        curr = q.popleft()
        for x, y in neighbors8(curr):
            if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                grid[x][y] += 1
                if grid[x][y] > 9 and (x, y) not in seen:
                    q.append((x, y))
                    seen.add((x, y))

    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            if grid[r][c] > 9:
                grid[r][c] = 0
                flashes += 1
    return grid, flashes


day11 = parse_input('data/input11.txt', parser=lambda s: list(map(int, s)), test=False)


def part1(iterations: int, stepfn: Callable, stuff: Tuple) -> int:
    grid, flashes = repeat(iterations, stepfn, stuff)
    return flashes


assert part1(100, recursive_step, (day11, 0)) == 1673
assert part1(100, recursive_step, (test_data11, 0)) == 1656


def part2(stuff: Tuple, stepfn: Callable) -> int:
    iteration = 0
    while True:
        grid, flashes = stepfn(stuff)
        iteration += 1
        if flashes == 100:
            break
        else:
            stuff = grid, 0
    return iteration


assert part2((test_data11, 0), iterative_step) == 95
assert part2((day11, 0), iterative_step) == 179
