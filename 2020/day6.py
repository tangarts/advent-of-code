#%%
from advent_of_code.core import *
from advent_of_code.debug import trace1


test_input = """abc

a
b
c

ab
ac

a
a
a
a

b
"""

test_input = parse_input(test_input, parser=str.splitlines, sep="\n\n")

with open("data/input6.txt") as f:
    _input = f.read()

_input = parse_input(_input, parser=str.splitlines, sep="\n\n")


def part1(groups):
    "count letters that anyone has"
    return sum(len(set("".join(group))) for group in groups)


assert part1(test_input) == 11
assert part1(_input) == 7027

### part 2


def part2(groups):
    "count letters that are common to everyone"
    return sum(len(set.intersection(*map(set, group))) for group in groups)


assert part2(test_input) == 6
print(part2(_input))

# %%
