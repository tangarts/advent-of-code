#%%
with open("data/input3.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]


def transpose(data):
    def col(grid, column):
        return [grid[row][column] for row in range(len(grid))]

    return ["".join(col(data, row)) for row in range(len(data[0]))]


data_t = transpose(data)

most_common_bit_string = "".join(
    [
        "1" if data_t[row].count("1") > len(data) // 2 else "0"
        for row in range(len(data[0]))
    ]
)

least_common_bit_string = "".join(
    ["0" if x == "1" else "1" for x in most_common_bit_string]
)

# %%
assert int(most_common_bit_string, 2) * int(least_common_bit_string, 2) == 3549854

### PART 2
# %%
def most_common(array: str) -> str:
    if array.count("1") >= len(array) - len(array) // 2:
        return "1"
    return "0"


def least_common(array: list) -> str:
    if array.count("1") < len(array) - len(array) // 2:
        return "1"
    return "0"


#%%
test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

#%%
def oxygen_rating(data):

    index = 0
    while len(data) > 1:
        data_t = transpose(data)
        mc = most_common(data_t[index])
        data = list(filter(lambda x: x[index] == mc, data))
        index += 1
    return data[0]


def co2_rating(data):
    index = 0
    while len(data) > 1:
        data_t = transpose(data)
        lc = least_common(data_t[index])
        data = list(filter(lambda x: x[index] == lc, data))
        index += 1
    return data[0]


#%%
assert int(oxygen_rating(data), 2) * int(co2_rating(data), 2) == 3765399

# %%
