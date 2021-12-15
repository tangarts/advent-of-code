#%%
from collections import deque
from typing import List, Tuple
import heapq
from advent_of_code.core import mapt, parse_input
from advent_of_code.point import neighbors4


raw = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

test = parse_input(raw, parser=lambda s: list(map(int, s)))


def dijkstra_search(
    graph: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]
):
    m, n = len(graph), len(graph[0])
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from: dict = {}
    cost_so_far: dict = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current: Tuple[int, int] = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for neighbour in neighbors4(current):
            x, y = neighbour
            if 0 <= x < m and 0 <= y < n:
                new_cost = cost_so_far[current] + graph[x][y]
                if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                    cost_so_far[neighbour] = new_cost
                    priority = new_cost
                    heapq.heappush(frontier, (priority, neighbour))
                    came_from[neighbour] = current

    return came_from, cost_so_far


# %%
came_from, cost_so_far = dijkstra_search(test, (0, 0), (9, 9))
# %%
def reconstruct_path(came_from: dict, start, goal) -> List:
    current = goal
    path: List = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


def search(graph):
    m, n = len(graph), len(graph[0])
    came_from, cost_so_far = dijkstra_search(test, (0, 0), (m, n))
    path = [graph[x][y] for x, y in reconstruct_path(came_from, (0, 0), (m, n))]
    return path


# %%
day15 = parse_input("data/input15.txt", parser=lambda s: list(map(int, s)), test=False)
# %%
m, n = len(day15) - 1, len(day15[0]) - 1
came_from, cost_so_far = dijkstra_search(day15, (0, 0), (m, n))
cost_so_far[(m, n)]
# %%

############## PART 2
# %%
test15 = parse_input("test15.txt", parser=lambda s: list(map(int, s)), test=False)
m, n = len(test15) - 1, len(test15[0]) - 1
came_from, cost_so_far = dijkstra_search(test15, (0, 0), (m, n))
cost_so_far[(m, n)]
# %%
def tile(graph):

    return graph


g0 = [[8]]
gg = [[8 for _ in range(5)] for _ in range(5)]
tile(g0) == [
    [8, 9, 1, 2, 3],
    [9, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
]


def update(g):
    for r, row in enumerate(g):
        for c, _ in enumerate(row):
            g[r][c] = rule(g[r][c])
    return g


def rule(x):
    if x < 9:
        return x + 1
    return 1


# %%
for i in range(1, 5):
    for j in range(1, 5):
        gg[i][j] = rule(gg[i][j - 1])
# %%
gg
# %%
