from collections import defaultdict

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

def data(_input, sep: str="\n", parser=str, test: bool=True):
    if not test:
        with open(_input) as f:
            _input = f.read()
    sections = _input.rstrip().split(sep)
    return [parser(section) for section in sections]

def count(iterable, predicate=bool):
    return sum(1 for item in iterable if predicate(item))

def mapt(fn, *args):
    "map(fn, *args) and return the result as a tuple."
    return tuple(map(fn, *args))

def str_to_tup(string):
    """
    convert string to tuple 
    example: str_to_tup('0, 0') => (0, 0)
    """
    return mapt(int, string.split(","))

def X(point): return point[0]
def Y(point): return point[1]

def count_points(p1: tuple, p2: tuple, part1=True):
    min_y, max_y = min(Y(p2), Y(p1)), max(Y(p2), Y(p1))
    min_x, max_x = min(X(p2), X(p1)), max(X(p2), X(p1))
    if X(p1) == X(p2):
        return [(X(p1), y) for y in range(min_y, max_y + 1)]
    elif Y(p1) == Y(p2):
        return [(x, Y(p1)) for x in range(min_x, max_x + 1)]
    elif not part1:
        grad = (max_y - min_y) / (max_x - min_x)
        c = min_y if grad > 0 else max_y
        return [(x, grad*x + c) for x in range(min_x, max_x + 1)]
    return []

def do(_input, istest, part1):
    point_map = defaultdict(int)
    _input = data(_input, 
                  parser=lambda s: mapt(str_to_tup, s.split(" -> ")), 
                  test=istest)

    for points in _input:
        p1, p2 = points
        px =count_points(p1, p2, part1)
        for p in px:
            point_map[p] += 1

    return count(point_map.values(), lambda c: c > 1)


assert do(test_input, True, part1=True) == 5
assert do('data/input5.txt', False, part1=True) == 6461


## part2

print(do(test_input, istest=True, part1=False))
assert do(test_input, istest=True, part1=False) == 12

