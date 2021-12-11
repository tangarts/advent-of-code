from advent_of_code.core import parse_input

input1 = parse_input('data/input1.txt', sep="\n", parser=int, test=False)

print(sum(input1))

frequency = {}

cumsum = 0
i = 0
while True:
    cumsum += input1[i]
    if cumsum in frequency:
        break
    frequency[cumsum] = 0
    
    if i == len(input1) - 1:
        i = 0
    else: 
        i += 1

print(cumsum)

