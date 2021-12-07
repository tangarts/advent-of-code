from heapq import heappop, heappush


def astar_search(start, h_func, moves_func):
    "Find a shortest sequence of states from start to a goal state (a state s with h_func(s) == 0)."
    frontier = [
        (h_func(start), start)
    ]  # A priority queue, ordered by path length, f = g + h
    previous = {start: None}  # start state has no previous state; other states will
    path_cost = {start: 0}  # The cost of the best path to a state.
    while frontier:
        (_, s) = heappop(frontier)
        if h_func(s) == 0:
            return Path(previous, s)
        for s2 in moves_func(s):
            new_cost = path_cost[s] + 1
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s
    return dict(fail=True, front=len(frontier), prev=len(previous))


def Path(previous, s):
    "Return a list of states that lead to state s, according to the previous dict."
    return [] if (s is None) else Path(previous, previous[s]) + [s]
