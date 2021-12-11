#%%
from typing import Union, List
from advent_of_code.core import parse_input

_test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

brackets = {"{": "}", "[": "]", "(": ")", "<": ">"}

test_input = parse_input(_test_input)
_input = parse_input("data/input10.txt", test=False)


def balanced_paren(string: str) -> Union[str, List[str]]:
    stack = []
    for char in string:
        if char in brackets:
            stack.append(brackets[char])
        elif stack and char == stack[-1]:
            stack.pop()
        else:
            return char
    return stack[::-1]


print([balanced_paren(t) for t in test_input])


def get_score(data: list) -> int:
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    illegals = tuple(
        filter(lambda x: isinstance(x, str), [balanced_paren(test) for test in data])
    )
    return sum(illegals.count(key) * value for key, value in points.items())


assert get_score(test_input) == 26397
print(get_score(_input))  # 415953


# %%
def get_score2(data: list) -> int:
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    incomplete = tuple(
        filter(lambda x: isinstance(x, list), [balanced_paren(test) for test in data])
    )

    def calculate_score(line: List[str]) -> int:
        score = 0
        for ket in line:
            score = score * 5 + points[ket]
        return score

    ##return sum(illegals.count(key) * value for key, value in points.items())
    scores = [calculate_score(l) for l in incomplete]
    return sorted(scores)[len(scores) // 2]


assert get_score2(test_input) == 288957
assert get_score2(_input) == 2292863731

# %%
