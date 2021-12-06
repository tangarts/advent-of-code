#%%
from advent_of_code.core import *
from collections import deque

#%%
_test_input = "3,4,3,1,2"
test_input = data(_test_input, sep=",", parser=int)

#%%
def simulate(fish: list, days: int) -> int:
    q = deque([fish.count(x) for x in range(9)])
    for _ in range(days):
        zeros = q.popleft()
        q.append(zeros)
        q[6] += zeros
    return sum(q)


#%%
print(simulate(test_input, 18))
assert simulate(test_input, 18) == 26
assert simulate(test_input, 80) == 5934

_input = data("data/input6.txt", sep=",", parser=int, test=False)

assert simulate(_input, 80) == 360268
assert simulate(test_input, 256) == 26984457539
simulate(_input, 256)

# %%
