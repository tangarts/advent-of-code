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
