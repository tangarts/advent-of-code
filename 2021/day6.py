from advent_of_code.core import *

_test_input = "3,4,3,1,2"

test_input = data(_test_input, sep=",", parser=int)

def tick(n: int) -> int:
    "apply lantern rule"
    if n > 0:
        return n - 1
    return 6

def simulate(fish: list, days: int):
    cache = {}
    for _ in range(days):
        zeros = fish.count(0)
        fish = list(map(tick, fish))
        fish += [8]*zeros
    return length(fish)

assert simulate(test_input, 18) == 26
assert simulate(test_input, 80) == 5934

_input = data('2021/data/input6.txt', sep=",", parser=int, test=False)

print(simulate(_input, 80))
#assert simulate(test_input, 256) == 26984457539
