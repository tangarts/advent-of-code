from advent_of_code.core import parse_input, integers

day17 = parse_input('data/input17.txt', parser=integers, test=False)[0]

test_input = parse_input("target area: x=20..30, y=-10..-5", parser=integers)

test_coords = integers("target area: x=20..30, y=-10..-5")


def step(pos_x, pos_y, vx, vy):
    """
    The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. 

    On each step, these changes occur in the following order:

    - The probe's x position increases by its x velocity.
    - The probe's y position increases by its y velocity.
    - Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    - Due to gravity, the probe's y velocity decreases by 1.
    """
    pos_x += vx
    pos_y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1

    return pos_x, pos_y, vx, vy


def iterate_probe_heights(ranges):
    max_heights = {}
    minx, maxx, miny, maxy = ranges
    xrange, yrange = range(minx, maxx + 1), range(miny, maxy + 1)
    for x0 in range(0, maxx + 1):
        for y0 in range(miny - 1, 200):
            pos_x, pos_y = (0, 0)
            vx, vy = x0, y0
            max_heights[(x0, y0)] = pos_y
            while pos_y > miny:
                pos_x, pos_y, vx, vy = step(pos_x, pos_y, vx, vy)
                max_heights[(x0, y0)] = max(max_heights[(x0, y0)], pos_y)
                if pos_x in xrange and pos_y in yrange:
                    break
                elif pos_x > maxx or pos_y <= miny:
                    del max_heights[(x0, y0)]
                    break
    return max_heights


# part 1
test_output = iterate_probe_heights(test_coords)
output = iterate_probe_heights(day17)

assert max(test_output.values()) == 45
assert max(output.values()) == 9870

# part2
assert len(output) == 5523
assert len(test_output) == 112
