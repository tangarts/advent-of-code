
from advent_of_code.core import parse_input

_test_input = "16,1,2,0,4,2,7,1,2,14"

test_input = parse_input(_test_input, sep=",", parser=int)

_input = parse_input('data/input7.txt', sep=",", parser=int, test=False) # 0 -> 1937


def get_position(data, distance_fn):
    pos = [0 for _ in range(max(data)+1)]
    for i in range(len(pos)):
        for fuel in (data):
            pos[i] += distance_fn(fuel, i)
    return min(pos)

def absolute(x: int, y: int) -> int:
    return abs(x - y)

def natural_sum(n: int) -> int:
    return n * (n + 1) // 2

def compose(f, g):
    return lambda *x: f(g(*x))

    
# assert get_position(test_input, absolute) == 37
print(get_position(test_input, absolute))
print(get_position(_input,  absolute))
# assert get_position(test_input) == 168

print(get_position(
    test_input, 
    compose(natural_sum, absolute)))

print(get_position(
    _input, 
    compose(natural_sum, absolute)))


