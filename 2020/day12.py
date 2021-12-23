#%%
from typing import List, Tuple
from advent_of_code.core import mapt, parse_input
from advent_of_code.point import manhattan_distance

raw = """F10
N3
F7
R90
F11"""


test = parse_input(raw, parser=lambda l: (l[0], int(l[1:])))
day12 = parse_input("data/input12.txt", parser=lambda l: (l[0], int(l[1:])), test=False)


COMPASS = "NESW"


def rotate(current: str, action: str, angle: int) -> str:
    """rotate through NESW by mapping 90 degree turns right to moving
    an position right in NESW
    left is the oppose direction
    """
    # can only rotate left or right
    assert action in "RL"

    idx = COMPASS.index(current)
    offset = angle // 90
    direction = 1 if action == "R" else -1
    return COMPASS[(idx + direction * offset) % 4]


def test_rotate() -> None:
    assert rotate("E", "R", 90) == "S"
    assert rotate("E", "L", 90) == "N"
    assert rotate("E", "L", 270) == "S"
    assert rotate("E", "R", 270) == "N"
    assert rotate("E", "R", 360) == "E"
    assert rotate("E", "L", 360) == "E"
    assert rotate("E", "R", 180) == "W"
    assert rotate("E", "L", 180) == "W"


def part1(instructions: List[Tuple[str, int]]) -> int:
    current = "E"
    directions = {k: 0 for k in COMPASS}
    for action, value in instructions:
        if action == "F":
            directions[current] += value
        elif action in "NESW":
            directions[action] += value
        elif action in "LR":
            current = rotate(current, action, value)

    return abs(directions["N"] - directions["S"]) + abs(
        directions["E"] - directions["W"]
    )


assert part1(test) == 25
assert part1(day12) == 1133

# part 2
def part2(instructions: List[Tuple[str, int]]) -> int:
    waypoint = {"E": 10, "N": 1, "W": 0, "S": 0}
    ship = {k: 0 for k in COMPASS}

    for action, value in instructions:
        if action == "F":
            for direction in "NESW":
                ship[direction] += value * waypoint[direction]
        elif action in "NESW":
            waypoint[action] += value
        elif action in "LR":
            waypoint = {rotate(k, action, value): val for k, val in waypoint.items()}

    return abs(ship["N"] - ship["S"]) + abs(ship["E"] - ship["W"])


assert part2(test) == 286
assert part2(day12) == 61053
