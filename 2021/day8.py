from advent_of_code.core import data, mapt, quantify

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

test_input1 = data(_test_input1, "\n", parser=lambda s: s.split(" | "))
test_input = data(_test_input, "\n", parser=lambda s: s.split(" | "))
_input = data('data/input8.txt', "\n", parser=lambda s: s.split(" | "), test=False)

# k : v -> segments on : digit
digits = {
        2: [1], 
        5: [2,3, 5], 
        4: [4], 
        3: [7],
        6: [0, 6, 9],
        7: [8]
    }


def part1(data):
    count = 0
    for _, output_value in data:
        segment = output_value.split(" ")
        count += quantify(segment, lambda s: len(s) in (2, 3, 4, 7))
    return count

assert part1(test_input) == 26
assert part1(_input) == 539

for _, output_value in test_input:
    segment = output_value.split(" ")
    quantify(segment, lambda s: len(s) in (2, 3, 4, 7))
 

