#%%
from advent_of_code.core import parse_input

raw = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def two_sum(array: list, t: int) -> int:
    cache = {}
    for i in range(len(array)):
        if array[i] not in cache:
            cache[t - array[i]] = array[i]
        else:
            return array[i] + cache[array[i]]
    return -1


test = parse_input(raw, parser=int)


# %%
def part1(numbers, window):

    for i in range(window + 1, len(numbers)):
        if two_sum(numbers[i - window : i ], numbers[i]) == -1:
            return numbers[i]


# %%
part1(test, 5)
# %%
day9 = parse_input("data/input9.txt", sep="\n", parser=int, test=False)
part1(day9, 25)
# %%
day9
# %%
