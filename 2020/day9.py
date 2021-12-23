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
        if two_sum(numbers[i - window : i], numbers[i]) == -1:
            return numbers[i]


day9 = parse_input("data/input9.txt", sep="\n", parser=int, test=False)

assert part1(test, 5) == 127
assert part1(day9, 25) == 1930745883

# %%
# part 2
# find a contiguous set of at least two numbers in
# your list which sum to the invalid number from step 1.


def part2(numbers, target):
    left, right = 0, 0
    total = 0
    while left < len(numbers) - 1 or right < len(numbers) - 1:

        while total < target:
            total += numbers[right]
            right += 1
        if total > target:
            total -= numbers[left]
            left += 1
        if total == target:
            return min(numbers[left:right]) + max(numbers[left:right])


# %%
assert part2(test, 127) == 62

assert part2(day9, 1930745883) == 268878261

# %%
