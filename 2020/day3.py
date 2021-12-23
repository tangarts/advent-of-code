"""
You start on the open square (.) in the top-left corner and need to reach the
bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper
model that prefers rational numbers); start by counting all the trees you would
encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3
and down 1. Then, check the position that is right 3 and down 1 from there, and
so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where
there was an open square and X where there was a tree:

In this example, traversing the map using this slope would cause you to
encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and
down 1, how many trees would you encounter?

"""


# %%
down = 0
trees = 0
right = 0
with open("data/input3.txt") as testf:
    board = [line.strip("\n") for line in testf.readlines()]
    # for line in testf.readlines():
    #     line = line.strip('\n')
    #     if line[right%(len(line))] == "#":
    #         trees += 1
    #     right += 3
    #     down += 1
# %%
def traverse(board, right, down):
    x = trees = 0
    for row in range(0, len(board), down):
        if board[row][x % len(board[0])] == "#":
            trees += 1
        x += right
    return trees


# %%
total = 1
for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    print(traverse(board, x, y))
    total *= traverse(board, x, y)
print(total)
# %%
[i for i in range(0, 10, 1)]
# %%
