from functools import lru_cache
from itertools import product
from advent_of_code.core import parse_input

raw = """Player 1 starting position: 4
Player 2 starting position: 8"""

test = parse_input(raw, parser=lambda s: int(s[-1]))
positions = parse_input('data/input21.txt', parser=lambda s: int(s[-1]), test=False)

def turn(position, roll):
    return (position + roll) % 10

def part1(position):
    # player, starting_pos
    score = [0, 0]
    roll = 0
    j = 1
    while True:
        for i in [0, 1]:
            roll += 3
            position[i] = turn(position[i], 3 * (j + 1))
            j = (j + 3) % 100
            score[i] += position[i] if position[i] != 0 else 10
            # when statement
            if score[i] > 999:
                return min(score) * roll


# part1
assert part1(positions) == 926610


all_states = [sum(x) for x in product([1, 2, 3], repeat=3)]
@lru_cache(maxsize=None)
def play(position1, position2, score1, score2):

    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1

    win1 = win2 = 0

    for state in all_states:
        new_position = turn(position1, state)
        new_score = score1 + (new_position if new_position else 10)
        w2, w1 = play(position2, new_position, score2, new_score)
        win1 += w1
        win2 += w2
    return win1, win2

# part2
assert max(play(6, 2, 0, 0)) == 146854918035875
