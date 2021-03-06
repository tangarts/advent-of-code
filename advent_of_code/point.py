# 2-D points implemented using (x, y) tuples
#%%
from typing import Tuple, Union

origin = (0, 0)
HEADINGS = UP, LEFT, DOWN, RIGHT = (0, -1), (-1, 0), (0, 1), (1, 0)


def X(point: Tuple[Union[float, int], Union[float, int]]) -> Union[float, int]:
    return point[0]


def Y(point: Tuple[Union[float, int], Union[float, int]]) -> Union[float, int]:
    return point[1]


def turn_right(heading):
    return HEADINGS[HEADINGS.index(heading) - 1]


def turn_around(heading):
    return HEADINGS[HEADINGS.index(heading) - 2]


def turn_left(heading):
    return HEADINGS[HEADINGS.index(heading) - 3]


# def add(A, B):
#     "Element-wise addition of two n-dimensional vectors."
#     return mapt(sum, zip(A, B))


def distance(P: Tuple[int, int], Q: Tuple[int, int] = origin) -> Union[float, int]:
    "Straight-line (hypotenuse) distance between two points."
    return sum((p - q) ** 2 for p, q in zip(P, Q)) ** 0.5


def king_distance(P: Tuple[int, int], Q: Tuple[int, int] = origin) -> float:
    "Number of chess King moves between two points."
    return max(abs(p - q) for p, q in zip(P, Q))


def neighbors4(point: Tuple[int, int]) -> Tuple[Tuple[int, int], ...]:
    "The four neighbors (without diagonals)."
    x, y = point
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def neighbors8(point: Tuple[int, int]) -> Tuple[Tuple[int, int], ...]:
    "The eight neighbors (with diagonals)."
    x, y = point
    return (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
    )


def manhattan_distance(
    P: Tuple[float, ...], Q: Union[Tuple[int, ...], None] = None
) -> Union[float, int]:
    "manhattan distance between two points"
    if Q is None:
        Q = (0 for _ in range(len(P)))
    return sum(abs(p - q) for p, q in zip(P, Q))
