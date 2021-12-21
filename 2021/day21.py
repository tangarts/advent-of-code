from advent_of_code.core import parse_input, integers

raw= """Player 1 starting position: 4
Player 2 starting position: 8"""

# player, starting_pos
score = {1: 0, 2: 0}

def turn(position, roll):
    return (position + roll) % 10

assert turn(7, 5) == 2
assert turn(4, 1+2+3) == 0
assert turn(10, 7+8+9) == 4

def part1(player1, player2):
    roll = 0
    j = 1
    while True:
        roll += 3
        player1 = turn(player1, 3*(j+1))
        j = (j + 3) % 100
        score[1] +=  player1 if player1 != 0 else 10
        if score[1] > 999:
            break
        roll += 3
        player2 = turn(player2, 3*(j+1))
        j = (j + 3) % 100
        score[2] +=  player2 if player2 != 0 else 10
        if score[2] > 999:
            break
    return min(score[1], score[2])*roll

print(part1(6, 2))


