from advent_of_code.core import parse_input, integers, quantify
from collections import Counter

raw_input = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""

test_input = parse_input(raw_input, parser=integers)


def overlapping_points(claims: list) -> dict:
    counter = Counter()
    for _, x, y, width, height in claims:
        points = Counter([(x + w, y + h) for w in range(width)
                          for h in range(height)])
        counter += points
    return counter


def count_overlapping(counter: dict) -> int:
    return quantify(counter, lambda p: counter[p] >= 2)


assert count_overlapping(overlapping_points(test_input)) == 4

day3 = parse_input('data/input3.txt', parser=integers, test=False)
# assert count_overlapping(overlapping_points(day3)) == 119572

# part 2

# zero overlap
def part2(data: list) -> int:
    overlapping = overlapping_points(data)
    for _id, x, y, width, height in data:
        points = [(x + w, y + h) for w in range(width) for h in range(height)]
        if all(overlapping[p] == 1 for p in points):
            return _id
    return -1
    

# print(part2(day3)) # 775

# NOTE: Very, very slow code. Can I revisit and optimize??
