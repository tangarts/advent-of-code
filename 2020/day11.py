#%%
import pytest
from collections import deque
from advent_of_code.point import neighbors8
from advent_of_code.core import parse_input, mapt

raw = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

test = parse_input(raw, parser=list)
day11 = parse_input("data/input11.txt", parser=list, test=False)

# %%
def seat(graph, i, j):
    m, n = len(graph), len(graph[0])
    nei = []
    for x, y in neighbors8((i, j)):
        if 0 <= x < m and 0 <= y < n:
            nei.append((x, y))
    # empty seats with zero "#" neighbours become "#"
    if graph[i][j] == "L" and [graph[n[0]][n[1]] for n in nei].count("#") == 0:
        return (i, j), "#"
    elif graph[i][j] == "#" and [graph[n[0]][n[1]] for n in nei].count("#") >= 4:
        return (i, j), "L"

    return (i, j), ""


def apply_seating(graph, seatfn):
    changes = {"#": [], "L": [], ".": []}
    for r, row in enumerate(graph):
        for c, _ in enumerate(row):
            pos, seat_type = seatfn(graph, r, c)
            if seat_type:
                changes[seat_type].append(pos)
    for k in changes:
        for p in changes[k]:
            x, y = p
            graph[x][y] = k

    return graph, sum(map(len, changes.values()))


def part1(graph):
    graph, changes = apply_seating(graph, seat)

    while changes > 0:
        graph, changes = apply_seating(graph, seat)

    return sum(
        1 if graph[x][y] == "#" else 0
        for x in range(len(graph))
        for y in range(len(graph[0]))
    )


assert part1(test) == 37
assert part1(day11) == 2299


## Part 2


def search_seat(graph, i, j, dx, dy):
    m, n = len(graph), len(graph[0])
    while 0 <= i + dx < m and 0 <= j + dy < n:
        i += dx
        j += dy
        if graph[i][j] in ["L", "#"]:
            return graph[i][j]
    return ""


DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


@pytest.mark.parametrize(
    "graph, x, y, expected",
    [
        (
            """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.""",
            3,
            3,
            [".", ".", ".", ".", ".", ".", ".", "."],
        ),
        (
            """.............
.L.L.#.#.#.#.
.............""",
            1,
            1,
            [".", "L", ".", ".", ".", ".", ".", "."],
        ),
        (
            """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....""",
            4,
            3,
            ["#", "#", "#", "#", "#", "#", "#", "#"],
        ),
    ],
)
def test_search_seat(graph, x, y, expected):
    graph = parse_input(graph, parser=list)
    assert [search_seat(graph, x, y, dx, dy) for dx, dy in DIRECTIONS] == expected


def seat2(graph, i, j):
    nei = [search_seat(graph, i, j, dx, dy) for dx, dy in DIRECTIONS]
    # empty seats with zero "#" neighbours become "#"
    if graph[i][j] == "L" and nei.count("#") == 0:
        return (i, j), "#"
    elif graph[i][j] == "#" and nei.count("#") >= 5:
        return (i, j), "L"

    return (i, j), ""


def part2(graph):
    graph, changes = apply_seating(graph, seat2)

    while changes > 0:
        graph, changes = apply_seating(graph, seat2)

    return sum(
        1 if graph[x][y] == "#" else 0
        for x in range(len(graph))
        for y in range(len(graph[0]))
    )


## Part2
assert part2(test) == 26
assert part2(day11) == 2047
