from advent_of_code.core import parse_input

# raw = """...>...
# .......
# ......>
# v.....>
# ......>
# .......
# ..vvv.."""

raw = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

test = parse_input(raw, parser=list)


def half_step(graph, i, j, cuke):
    m, n = len(graph), len(graph[0])
    "see if a cucumber can move"
    if graph[i][j] == "v" and cuke == "v":
        if graph[(i + 1) % m][j] == ".":
            return (i, j), ((i + 1) % m, j), "v"
    if graph[i][j] == ">" and cuke == ">":
        if graph[i][(j+1) % n] == ".":
            return (i, j), (i, (j + 1) % n), ">"
    return (i, j), (i, j), ""

def full_step(graph):
    update = {">": [], "v": []}
    for cuke in ">v":
        for r, row in enumerate(graph):
            for c, _ in enumerate(row):
                oldpos, pos, c = half_step(graph, r, c, cuke)
                if c:
                    update[c].append((oldpos, pos))
        
        for positions in update[cuke]:
            old, new = positions
        
            graph[old[0]][old[1]] = "."
            graph[new[0]][new[1]] = cuke
    return graph, sum(map(len, update.values()))

def part1(graph):
    graph, changes = full_step(graph)
    count = 1
    while changes > 0:
        graph, changes = full_step(graph)
        count += 1

    return count

# assert part1(test) == 58

day25 = parse_input('data/input25.txt', parser=list, test=False)

print(part1(day25))



