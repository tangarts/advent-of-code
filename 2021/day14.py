#%%
from collections import defaultdict
from typing import Counter
from advent_of_code.core import parse_input, repeat
from advent_of_code.other import overlapping

# similar vibes to lanternfish
# We will not track the count in array but count the
# PAIRS 'NN', 'NC', 'CB' in a dictionary

raw_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def to_pairs(string: str):
    first, second = string.split(" -> ")
    pairs = first[0] + second, second + first[1]
    return first, pairs


template, insertion = raw_input.split("\n\n")
# %%
insertion_map = dict(parse_input(insertion, sep="\n", parser=to_pairs))
character_map = dict(parse_input(insertion, sep="\n", parser=lambda s: s.split(" -> ")))

# %%
def step(counter, char_map, insertion_map):
    changes = []

    for key, value in counter.items():
        if key in insertion_map and counter[key] > 0:
            changes.append((key, -value))
            for v in insertion_map[key]:
                changes.append((v, value))

    for key, size in changes:
        counter[key] += size
        if size < 0:
            char_map[character_map[key]] += -size

    return counter, char_map


def dotimes(n, c, cmap, imap):
    for i in range(n):
        c, cmap = step(c, cmap, imap)
    return c, cmap


# %%
template, insertion = parse_input("data/input14.txt", sep="\n\n", test=False)
# %%
insertion_map = dict(parse_input(insertion, sep="\n", parser=to_pairs))
character_map = dict(parse_input(insertion, sep="\n", parser=lambda s: s.split(" -> ")))

c, cmap = dotimes(
    10, c=Counter(overlapping(template, 2)), cmap=Counter(template), imap=insertion_map
)
# %%
cmap
# %%
3092 - 717
# %%
c, cmap = dotimes(
    40, c=Counter(overlapping(template, 2)), cmap=Counter(template), imap=insertion_map
)
# %%
def answer(n):
    return max(cmap.values()) - min(cmap.values())


# %%
