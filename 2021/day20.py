
from advent_of_code.core import parse_input, flatten

raw = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

test_enhance, test_input_image = parse_input(raw, sep="\n\n", parser=lambda s: s.replace("#", "1").replace(".", "0"))
test_enhance = "".join(test_enhance.replace("\n", ""))
test_input_image = [list(i) for i in test_input_image.split("\n")]


def pad(matrix: list, i) -> list:
    """add zeros to matrix represented as List[str]
        "['010', '100', '110']" -> ["00000", "00100", "01000", "01100"]
    """
    matrix = [[str(i), *row, str(i)] for row in matrix]
    n = len(matrix[0])
    return [[str(i) for _ in range(n)]] + matrix + [[str(i) for _ in range(n)]]


def kernel(matrix, point, background="0"):
    m, n = len(matrix), len(matrix[0])
    pixels = []
    x, y = point
    # get binary string using kernel
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                   (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if 0 <= dx + x < m and 0 <= dy + y < n:
            pixels.append(matrix[x + dx][y + dy])
        else:
            pixels.append(background)
    index = int("".join(pixels), 2)
    return (point, index)


def enhance_pixels(matrix, indexes, enhance):
    for point, index in indexes.items():
        x, y = point
        pixel = enhance[index]
        matrix[x][y] = pixel
    return matrix


def new_pixels(matrix, background):
    indexes = dict()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            point, index = kernel(matrix, (i, j), background)
            indexes[point] = index
    return indexes


def enhance_image(matrix, enhance, background):
    matrix = pad(matrix, background)
    pixels = new_pixels(matrix, background)
    matrix = enhance_pixels(matrix, pixels, enhance)
    return matrix


def run(matrix, enhance, n):
    for i in range(n):
        matrix = enhance_image(matrix, enhance, str(i % 2))
    return list(flatten(matrix)).count("1")


def print_matrix(matrix):
    print("\n".join(["".join(i) for i in matrix]))


enhance, input_image = parse_input('data/input20.txt', sep="\n\n",
                                   parser=lambda s: s.replace("#", "1").replace(".", "0"), test=False)  # 5326
enhance = "".join(enhance.replace("\n", ""))
input_image = [list(i) for i in input_image.split("\n")]

# part 1
assert run(input_image, enhance, 2) == 5583

# part 2
# print(run(input_image, enhance, 50))
