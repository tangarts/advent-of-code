# Another graph traversal
from collections import defaultdict, deque
from typing import Callable

from advent_of_code.core import parse_input

raw_test = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_input = parse_input(raw_test, parser=lambda s: s.split("-"))

def build_graph(nodes: list) -> dict:
    graph = defaultdict(list)
    for u, v in nodes:
        graph[u].append(v)
        graph[v].append(u)
    return graph

graph1 = build_graph(test_input)

def part1_visited(node: str, path: list) -> bool:
    return node not in path or node.isupper()

def bfs(graph: dict, start: str, visited: Callable) -> int:
    # instead of nodes we want to keep track of entire paths
    paths = 0
    q = deque([[start]])
    while q:
        current_path = q.popleft()
        last_visited = current_path[-1]
        if last_visited == 'end': 
            paths += 1
        else:
            for neighbour in graph[last_visited]:
                if visited(neighbour, current_path):
                    next_path = current_path.copy()
                    next_path.append(neighbour)
                    q.append(next_path)

    return paths
            
assert bfs(graph1, 'start', part1_visited) == 10

example2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

graph2 = build_graph(parse_input(example2, parser=lambda s: s.split('-')))

assert bfs(graph2, 'start', part1_visited) == 19

example3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

graph3 = build_graph(parse_input(example3, parser=lambda s: s.split('-')))

assert bfs(graph3, 'start', part1_visited) == 226


day12 = parse_input('data/input12.txt',  parser=lambda s: s.split('-'), test=False)
graph = build_graph(day12)

assert bfs(graph, 'start', part1_visited) == 5178

def part2_visited(node: str, path: list) -> bool:
    # missed edge case
    if node == "start":
        return False
    ## small single cave
    # either revisit if node in path and all others have been visited once
    return part1_visited(node, path) or max(path.count(node) for node in path if node.islower()) == 1


assert bfs(graph1, 'start', part2_visited)  == 36
assert bfs(graph2, 'start', part2_visited)  == 103
assert bfs(graph3, 'start', part2_visited)  == 3509
assert bfs(graph, 'start', part2_visited) == 130094
