"""
Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to
2020; what do you get if you multiply them together?
 """

with open("data/input1.txt") as f:
    array = [int(s) for s in f.readlines()]


def two_sum(array: list, t: int = 2020) -> int:
    cache = {}
    for i in range(len(array)):
        if array[i] not in cache:
            cache[t - array[i]] = array[i]
        else:
            return array[i] * cache[array[i]]
    return -1


# print(two_sum(array))

"""
Using the above example again, the three entries that sum to 2020 are 979, 366,
and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to
2020?
"""

# Three sum

for a in array:
    if two_sum(array, 2020 - a):
        print(a * two_sum(array, 2020 - a))
