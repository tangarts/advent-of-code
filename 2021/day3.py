
#%%
with open('data/input3.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

data
# %%
def col(grid, column):
    return [grid[row][column] for row in range(len(grid))]


# %%
most_common_bit_string  = ''.join(["1" if col(data, row).count('1') > len(data) // 2 else "0"
    for row in range(len(data[0]))])

least_common_bit_string = ''.join(["0" if x == "1" else "1" for x in most_common_bit_string])

# %%
int(most_common_bit_string, 2) * int(least_common_bit_string, 2)
# %%
