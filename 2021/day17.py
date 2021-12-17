from advent_of_code.core import parse_input, integers
from advent_of_code.debug import trace1

day17 = parse_input('data/input17.txt', parser=integers, test=False)[0]

test_input = parse_input("target area: x=20..30, y=-10..-5", parser=integers)

test_coords = integers("target area: x=20..30, y=-10..-5")
coords = day17

def sign(x: int) -> int:
    if x > 0:
        return 1
    return -1

# @trace1
def step(pos_x, pos_y, vx, vy):
    """
    The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

    The probe's x position increases by its x velocity.
    The probe's y position increases by its y velocity.
    Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    Due to gravity, the probe's y velocity decreases by 1.
    """
    pos_x += vx
    pos_y += vy
    if vx > 0:
        vx -= 1
    else:
        vx += 1
    vy -= 1

    return pos_x, pos_y, vx, vy

seen = set()
max_heights = {}
minx, maxx, miny, maxy = test_coords
xrange, yrange = range(minx, maxx + 1), range(miny, maxy + 1)
for x in range(0, 800):
    for y in range(-600, 600):
        pos_x, pos_y = (0, 0)
        vx, vy = x, y
        max_heights[(x, y)] = pos_y
        for _ in range(1000):
            pos_x, pos_y, vx, vy = step(pos_x, pos_y, vx, vy)
            max_heights[(x, y)] = max(max_heights[(x, y)], pos_y)
            if pos_x in xrange and pos_y in yrange:
                seen.add((x, y))
                break
            elif pos_x > maxx or pos_y < miny:
                del max_heights[(x, y)]
                break
                        
### part 1
print(max(max_heights.values()))


### part2
print(len(seen))
