from collections import Counter

test_input = """abc

a
b
c

ab
ac

a
a
a
a

b
"""
test_input = test_input.split('\n\n')

with open('data/input6.txt') as f:
    _input = f.read()

_input = _input.split('\n\n')

groups = lambda _input: sum(len(Counter(group.replace("\n",""))) for group in _input) 

assert groups(test_input) == 11
# 7027
assert groups(_input) == 7027

