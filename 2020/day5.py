
def get_row(array):
    x = range(0, 128)
    for char in array:
        if char == 'F':
            x = x[:len(x)//2]
        elif char == 'B':
            x = x[len(x)//2:]
        else:
            ValueError
    return x[0]

assert get_row('FBFBBF') == 44

def get_col(array):
    x = range(0, 8)
    for char in array:
        if char == 'R':
            x = x[len(x)//2:]
        elif char == 'L':
            x = x[:len(x)//2]
        else:
            ValueError
    return x[0]

assert get_col('RLR') == 5

def seat_id(boarding_pass):
    left, right = boarding_pass[:7], boarding_pass[7:]
    return get_row(left) * 8 + get_col(right)

assert seat_id('FBFBBFFRLR') == 357

with open('data/input5.txt') as f:
    _input = [l.strip() for l in f.readlines()]

print(max(map(lambda x: seat_id(x), _input)))


### find the first missing seat
print(max(map(lambda x: seat_id(x), _input)))
