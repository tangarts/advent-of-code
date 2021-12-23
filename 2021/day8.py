#%%

from collections import Counter
from advent_of_code.core import parse_input, multimap, quantify

_test_input1 = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

_test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

test_input1 = parse_input(_test_input1, "\n", parser=lambda s: s.split(" | "))
test_input = parse_input(_test_input, "\n", parser=lambda s: s.split(" | "))
_input = parse_input("data/input8.txt", "\n", parser=lambda s: s.split(" | "), test=False)

# k : v -> segments on : digit
digits = {2: [1], 5: [2, 3, 5], 4: [4], 3: [7], 6: [0, 6, 9], 7: [8]}

#%%
def sortstr(sequence) -> str:
    "returns sorted sequence as string"
    return "".join(sorted(sequence))


def part1(data):
    count = 0
    for _, output_value in data:
        segment = output_value.split(" ")
        count += quantify(segment, lambda s: len(s) in (2, 3, 4, 7))
    return count


assert part1(test_input) == 26
assert part1(_input) == 539

#%%
def len_str_dict(segments):
    segment = segments.split(" ")
    return multimap([(len(s), sortstr(s)) for s in segment])


# %%
def get3(fives: list, one: str) -> set[str]:
    return set.intersection(*map(set, fives)).union(set(one))  # 3


# %%
def get9(sixes: list, four: str) -> set[str]:
    return set.intersection(*map(set, sixes)).union(set(four))  # 9


# %%
def get0(eight: str, three: str, four: str, one: str):
    return set(eight).difference(
        set(three).intersection(set(four)).difference(set(one))
    )  # 0


#%%
def get2(eight: str, five: str, fives: list):
    return (
        set(eight).difference(set(five)).union(set.intersection(*map(set, fives)))
    )  # 2


#%%
def get5(six: str, nine: str):
    return set(nine).intersection(set(six))  # 5


def get_digits(digits: list, digit_pattern: dict) -> int:
    return int(''.join([digit_pattern[d] for d in digits]))


#%%
count = 0
for _, output_value in test_input:
    # create hash map of (str.len, str)
    len_output = len_str_dict(output_value)
    # count the number of str with len 2,3,4 and 7
    for k in (2, 3, 4, 7):
        count += len(len_output.get(k, []))
count

#%%
## alternative part 1
counter = 0
for pattern, output_value in _input:
    digit_patterns = {}
    len_output = len_str_dict(pattern)
    # focus on the easy digits
    one = len_output[2][0]
    seven = len_output[3][0]
    four = len_output[4][0]
    eight = len_output[7][0]
    three = sortstr(get3(len_output[5], one))
    nine = sortstr(get9(len_output[6], four))
    zero = sortstr(get0(eight, three, four, one))
    six = [x for x in len_output[6] if x != zero and x != nine][0]
    five = sortstr(get5(six, nine))
    two = sortstr(get2(eight, five, len_output[5]))
    digit_patterns[one] = "1"
    digit_patterns[seven] = "7"
    digit_patterns[four] = "4"
    digit_patterns[eight] = "8"
    digit_patterns[two] = "2"
    digit_patterns[three] = "3"
    digit_patterns[five] = "5"
    digit_patterns[six] = "6"
    digit_patterns[nine] = "9"
    digit_patterns[zero] = "0"
    value = [sortstr(s) for s in output_value.split(" ")]
    counter += get_digits(value, digit_patterns)

print(counter)
