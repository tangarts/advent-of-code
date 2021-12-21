#%%
from functools import lru_cache
from itertools import product
from advent_of_code.core import parse_input, integers

raw = """Player 1 starting position: 4
Player 2 starting position: 8"""

test = dict(parse_input(raw, parser=integers))
test


def turn(position, roll):
    return (position + roll) % 10


assert turn(7, 5) == 2
assert turn(4, 1 + 2 + 3) == 0
assert turn(10, 7 + 8 + 9) == 4


def part1(player):
    # player, starting_pos
    score = {1: 0, 2: 0}

    roll = 0
    j = 1
    while True:
        for i in [1, 2]:
            roll += 3
            player[i] = turn(player[i], 3 * (j + 1))
            j = (j + 3) % 100
            score[i] += player[i] if player[i] != 0 else 10
            # when statement
            if score[i] > 999:
                return min(score[1], score[2]) * roll


print(part1(test))

#%%

# splits into 3 universes
# BUT there are only 7 different values for each roll
# 3..9 calculated from rolls (1,1,1) ... (3,3,3)
states = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
all_states = [sum(x) for x in product([1, 2, 3], repeat=3)]
#%%
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


#%%


# %%
play(4, 8, 0, 0)

# %%
max(play(2, 6, 0, 0))  # 273042027784929
