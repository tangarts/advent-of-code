import pytest
import re
from advent_of_code.core import mapt, parse_input
from itertools import permutations
from typing import List


def tokenize(numbers: str) -> list:
    "return token of integers and square brackets"
    tokens = [token for token in re.findall(r"\[|\]|[0-9]", numbers)]
    return [int(t) if "0" <= t <= "9" else t for t in tokens]


def add(l1: List, l2: List) -> List:
    return ["[", *l1, *l2, "]"]


def explode(numbers: list, i: int) -> list:
    """If any pair is nested inside four pairs, the leftmost such pair explodes.

    To explode a pair, the pair's left value is added to the first regular number
    to the left of the exploding pair (if any), and the pair's right value is added
    to the first regular number to the right of the exploding pair (if any).
    Exploding pairs will always consist of two regular numbers. Then, the entire
    exploding pair is replaced with the regular number 0.

    Examples:

        - [[[[**[9,8]**,1],2],3],4] becomes [[[**[0,9]**,2],3],4]
        - [7,[6,[5,[4,**[3,2]**]]]] becomes [7,[6,[5,**[7,0]**]]]
        - [[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3]
        - [[3,[2,[1,**[7,3]**]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,**[8,0]**]],[**9**,[5,[4,[3,2]]]]]

    """

    left_val, right_val = numbers[i + 1], numbers[i + 2]
    left_index, right_index = i+1, i + 2
    while left_index > 0:
        left_index -= 1
        if isinstance(numbers[left_index], int):
            numbers[left_index] += left_val
            break
    while right_index < len(numbers) - 1:
        right_index += 1
        if isinstance(numbers[right_index], int):
            numbers[right_index] += right_val
            break
    numbers = numbers[:i] + [0] + numbers[i + 4 :]
    return numbers


def split(numbers: list, i) -> list:
    """If any regular number is 10 or greater, the leftmost such regular number splits.

    To split a regular number, replace it with a pair;
    the left element of the pair should be the regular number divided by two and rounded down,
    while the right element of the pair should be the regular number divided by two and rounded up.

    For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.

    """
    assert numbers[i] >= 10
    numbers = (
        numbers[:i]
        + ["[", numbers[i] // 2, (numbers[i]+1) // 2, "]"]
        + numbers[i + 1 :]
    )
    return numbers


def action(numbers: list) -> list:
    depth = 0
    # either do explode or split
    # if neither then we know we should do
    # another add
    for i in range(len(numbers)):
        if numbers[i] == "[":
            depth += 1

        elif numbers[i] == "]":
            depth -= 1

        if depth == 5:
            return explode(numbers, i)

    for j, token in enumerate(numbers):
        if isinstance(token, int) and token >= 10:
            return split(numbers, j)

    return []



def doreduce(numbers: list) -> list:
    while True:
        temp = action(numbers)
        if temp != []:
            numbers = temp
        else:
            break
    return numbers

def test_action():
    assert action(tokenize("[[[[[9,8],1],2],3],4]")) == tokenize("[[[[0,9],2],3],4]")
    assert action(tokenize("[7,[6,[5,[4,[3,2]]]]]")) == tokenize("[7,[6,[5,[7,0]]]]")
    assert action(tokenize("[[6,[5,[4,[3,2]]]],1]")) == tokenize("[[6,[5,[7,0]]],3]")

def test_doreduce():

    assert doreduce(tokenize("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")) == tokenize( "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")

    assert (doreduce(tokenize("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"))) == tokenize("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")

def reduce_list(numbers: List) -> List:
    result = numbers[0]
    for x in numbers[1:]:
        result = add(result, x)
        result = doreduce(result)
    return result

raw_test1 = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
test1 = parse_input(raw_test1, parser=tokenize)

assert reduce_list(test1) == tokenize("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")

raw_test2 = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""


test2 = parse_input(raw_test2, parser=tokenize)

def magnitude(numbers):
    if len(numbers) <= 1:
        return numbers[0]
    for i in range(len(numbers)-1):
        if isinstance(numbers[i], int) and isinstance(numbers[i+1], int):
            numbers = numbers[:i-1]  + [3*numbers[i] + 2*numbers[i+1]] + numbers[i+3:]
            return magnitude(numbers)
    return -1

def test_magnitude():
    assert magnitude(tokenize("[9,1]")) == 29
    assert magnitude(tokenize("[[9,1],[1,9]]")) == 129
    assert magnitude(tokenize("[[1,2],[[3,4],5]]")) == 143
    assert magnitude(tokenize("[[[[3,0],[5,3]],[4,4]],[5,5]]")) == 791

    assert magnitude(tokenize("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]")) == 4140


day18 = parse_input('data/input18.txt', parser=tokenize, test=False)
assert magnitude(reduce_list(test1)) == 3488

# part 1
assert magnitude(reduce_list(day18)) == 4111

# part 2
def part2(numbers: list):
    return max(mapt(magnitude, [reduce_list([x, y]) for x, y in permutations(numbers, 2)]))

assert part2(test2) == 3993
print(part2(day18))
