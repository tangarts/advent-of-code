#%%
from typing import List, Tuple
from advent_of_code.core import parse_input

raw = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def parser(line: str) -> Tuple[str, int]:
    op, arg = line.split(" ")
    return op, int(arg)


test = parse_input(raw, parser=parser)
day8 = parse_input("data/input8.txt", parser=parser, test=False)


def part1(instructions: List[Tuple[str, int]]) -> int:
    i = 0
    acc = 0
    counter = [0 for _ in range(len(instructions))]
    while True:
        if counter[i] == 1:
            break
        op, arg = instructions[i]
        if op == "acc":
            acc += arg
            counter[i] += 1
            i += 1
        elif op == "jmp":
            counter[i] += 1
            i += arg
        else:
            counter[i] += 1
            i += 1

    return acc


# %%
assert part1(test) == 5
# %%
part1(day8)
# %%
