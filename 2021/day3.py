
#%%
with open('data/input3.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

data
# %%
def col(grid, column):
    return [grid[row][column] for row in range(len(grid))]


# %%

# %%
