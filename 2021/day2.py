#%%
with open("data/input2.txt", "r") as f:
    forward = depth = 0
    for lines in f.readlines():
        dirs, size = lines.split()
        size = int(size)
        if dirs == "down":
            depth += size
        elif dirs == "up":
            depth -= size
        elif dirs == "forward":
            forward += size

    assert forward * depth == 1989265
    print("Part 1: Pass")

# %%
with open("data/input2.txt", "r") as f:
    aim = forward = depth = 0
    for lines in f.readlines():
        dirs, size = lines.split()
        size = int(size)
        if dirs == "down":
            aim += size
        elif dirs == "up":
            aim -= size
        elif dirs == "forward":
            forward += size
            depth += size * aim

    assert forward * depth == 2089174012
    print("Part 2: Pass")

# %%
