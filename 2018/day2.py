from collections import Counter
from advent_of_code.core import parse_input

_test2 = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""

test2 = parse_input(_test2, parser=Counter)

def twos_and_threes(_input):
    twos = threes = 0
    for counters in _input:
        if 3 in counters.values():
            threes += 1
        if 2 in counters.values():
            twos += 1
    return twos, threes


threes, twos = twos_and_threes(test2)
assert threes * twos == 12

input2 = parse_input('data/input2.txt', parser=Counter, test=False)

threes, twos = twos_and_threes(input2)
# print(threes * twos) # 6916

def off_by_one(string1: str, string2: str) -> bool:
    diff = 0
    for s1, s2 in zip(string1, string2):
        if s1 != s2:
            diff += 1
    return diff == 1

def common_letters(string1: str, string2: str) -> str:
    return ''.join(s1 for s1, s2 in zip(string1, string2) if s1 == s2)

def part2(data: list) -> str:
    for i in range(len(data)):
        for j in range(i, len(data)):
            if off_by_one(data[i], data[j]):
                return common_letters(data[i], data[j])
    return ""

input2part2 = parse_input('data/input2.txt', test=False)
print(part2(input2part2))
