from advent_of_code.core import *

_test_input = "16,1,2,0,4,2,7,1,2,14"

test_input = data(_test_input, sep=",", parser=int)

_input = data('data/input7.txt', sep=",", parser=int, test=False) # 0 -> 1937


def get_position(_data):
    pos = [0 for _ in range(max(_data)+1)]
    for i in range(len(pos)):
        for fuel in _data:
            pos[i] += abs(fuel - i)
    return min(pos)

print(get_position(test_input))
assert get_position(test_input) == 37
print(get_position(_input))

# 345254
