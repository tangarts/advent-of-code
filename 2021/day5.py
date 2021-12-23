
from collections import defaultdict
from advent_of_code.core import parse_input, mapt

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def count(iterable, predicate=bool):
    return sum(1 for item in iterable if predicate(item))


def str_to_tup(string):
    """
    convert string to tuple
    example: str_to_tup('0, 0') => (0, 0)
    """
    return mapt(int, string.split(","))


def X(point):
    return point[0]


def Y(point):
    return point[1]


def count_points(p1: tuple, p2: tuple, part1=True):
    min_y, max_y = min(Y(p2), Y(p1)), max(Y(p2), Y(p1))
    min_x, max_x = min(X(p2), X(p1)), max(X(p2), X(p1))
    if X(p1) == X(p2):
        return [(X(p1), y) for y in range(min_y, max_y + 1)]
    elif Y(p1) == Y(p2):
        return [(x, Y(p1)) for x in range(min_x, max_x + 1)]

    if not part1:
        grad = (Y(p2) - Y(p1)) / (X(p2) - X(p1))
        return [(x, grad * (x - min_x) + Y(p1)) for x in range(min_x, max_x + 1)]
    return []


def do(_input, istest, part1):
    point_map = defaultdict(int)
    _input = parse_input(
        _input, parser=lambda s: mapt(str_to_tup, s.split(" -> ")), test=istest
    )

    for points in _input:
        p1, p2 = points
        if X(p1) > X(p2):
            p1, p2 = p2, p1
        px = count_points(p1, p2, part1)
        for p in px:
            point_map[p] += 1

    return count(point_map.values(), lambda c: c > 1)


# assert do(test_input, True, part1=True) == 5
# assert do('data/input5.txt', False, part1=True) == 6461


## part2

assert do(test_input, istest=True, part1=False) == 12
assert do("data/input5.txt", istest=False, part1=False) == 18065

# %%
