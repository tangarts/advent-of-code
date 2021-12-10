from advent_of_code.core import data

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

brackets = {"{":"}", "[":"]", "(":")", "<":">"}

test_input = data(_test_input)
_input = data('data/input10.txt', test=False)

def balanced_paren(string: str) -> str:
    stack = []
    for char in string:
        if char in brackets:
            stack.append(brackets[char])
        elif stack and char == stack[-1]:
            stack.pop()
        else:
            return char
    return ""

def get_score(data: list) -> int:
    points  = {")": 3, "]": 57, "}": 1197, ">": 25137}
    illegals = [balanced_paren(test) for test in data]
    return sum(illegals.count(key)*value for key,value in points.items())

assert get_score(test_input) == 26397
print(get_score(_input)) # 415953

