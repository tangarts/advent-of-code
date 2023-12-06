#%%
import re
from math import prod

data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


# %%
BAG = {"red" : 12, "green": 13, "blue": 14}

def getId(line):
    game, cubes = line.split(": ")
    id = int(game.strip("Game "))
    for round in cubes.split(";"):
        d = {"red" : 0, "green" : 0, "blue": 0}
        for record in re.findall(r'\d+\s\w+', round):
            i, key = record.split(" ")
            d[key] += int(i)
        if not (d["blue"] <= 14 and d["green"] <= 13 and d["red"] <= 12):
            return 0
    
    return id


# %%
print(sum(getId(l) for l in data.split("\n")))

# %%
#%%
with open("data/input2.txt", 'r') as f:
    data_list = [line.strip() for line in f.readlines()]
# %%
print(sum(getId(l) for l in data_list))

# %%
def getId2(line):
    game, cubes = line.split(": ")
    id = int(game.strip("Game "))
    d = {"red" : 0, "green" : 0, "blue": 0}
    for round in cubes.split(";"):
        for record in re.findall(r'\d+\s\w+', round):
            i, key = record.split(" ")
            d[key] = max(int(i), d[key])    
    return d
# %%
assert sum(prod(getId2(l).values()) for l in data.split("\n")) == 2286


# %%
assert sum(prod(getId2(l).values()) for l in data_list) == 66027


# %%
