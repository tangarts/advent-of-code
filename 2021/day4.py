
test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""



def parse_input(_input):
    _input = _input.split('\n\n')
    numbers, boards = _input[0], _input[1:]
    boards = [b.replace("\n", " ").replace("  ", " ").lstrip().rstrip().split(" ") for b in boards]
    boards = [list(map(int, row)) for row in boards]
    numbers = [int(num) for num in numbers.split(",")]

    return boards, numbers

def is_winner(board_index: set) -> bool:
    WINNING_INDEX =  [set([x + 5*y for x in range(5)]) for y in range(5)] \
             + [set([5*x + y for x in range(5)]) for y in range(5)]
    for indexes in WINNING_INDEX:
        if indexes.issubset(board_index):
            return True
    return False

def get_winner(boards, numbers):
    number_set = {i : set() for i in range(len(boards))}
    seen = []
    winner = []
    for num in numbers:
        for i, board in enumerate(boards):
            if num in board:
                number_set[i].add(board.index(num))
            if is_winner(number_set[i]) and i not in seen:
                seen.append(i)
                seen_idx = number_set[i]
                winner.append((board, seen_idx, num))
                if len(winner) == len(boards):
                    return board, seen_idx, num
    return winner[-1]

boards, numbers = parse_input(test_input)
board, num_set, last_num = get_winner(boards, numbers)
def score(board, idx, last_num):
    unmarked = [board[i] for i in set(range(25)) - idx]
    return sum(unmarked) * last_num

def part1(_input):
    boards, numbers = parse_input(_input)
    board, num_set, last_num = get_winner(boards, numbers)
    return score(board, num_set, last_num)

assert part1(test_input) == 1924#4512
with open('data/input4.txt') as f:
    data = f.read()

print(part1(data))

