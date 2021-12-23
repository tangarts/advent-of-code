import re
from itertools import combinations
from typing import Sequence, Tuple
from advent_of_code.core import mapt, parse_input, flatten
from advent_of_code.point import distance


def strip_scanner(scanner):

    _id, *coords = scanner.split("\n")
    _id = int(re.findall(r"[0-9]+", _id)[0])
    coords = mapt(lambda s: mapt(int, s.split(",")), coords)
    return _id, coords


def get_pairwise(points, _id) -> dict:
    return {distance(p, q): sorted([p, q])
            for p, q in combinations(points[_id], 2)}


def translate(points: Tuple[int, int, int]) -> Sequence[Tuple[int, int, int]]:
    x, y, z = points
    return (
        (x, y, z), (-x, y, z), (x, -y, z), (x, y, -z),
        (x, z, y), (-x, z, y), (x, -z, y), (x, z, -y),
        (y, x, z), (-y, x, z), (y, -x, z), (y, x, -z),
        (y, z, x), (y, -z, x), (y, z, -x), (-y, -z, -x),
        (z, y, x), (-z, y, x), (z, -y, x), (z, y, -x), (-z, -y, -x),
        (z, x, y), (-z, x, y), (z, -x, y), (z, x, -y), (-z, -x, -y),
    )



raw3d = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""

test3d = dict(parse_input(raw3d, sep="\n\n", parser=strip_scanner))

pairwise_distances = [get_pairwise(test3d, i) for i in test3d]


def overlapping(d1: set, d2: set) -> bool:
    return len([i for i in d1 & d2 
        # if i <= 1500
        ]) >= 12

o1 = """-618,-824,-621
-537,-823,-458
-447,-329,318
404,-588,-901
544,-627,-890
528,-643,409
-661,-816,-575
390,-675,-793
423,-701,434
-345,-311,381
459,-707,401
-485,-357,347"""

o2 = """686,422,578
605,423,415
515,917,-361
-336,658,858
-476,619,847
-460,603,-452
729,430,532
-322,571,750
-355,545,-477
413,935,-424
-391,539,-444
553,889,-390"""
o1 = o1.split("\n")
o2 = o2.split("\n")

o1 = mapt(lambda s: mapt(int, s.split(",")), o1)
o2 = mapt(lambda s: mapt(int, s.split(",")), o2)

print(o2)

origin = (0, 0, 0)
s0 = (-618,-824,-621)
s1 = (686,422,578)
b = [x-y for x, y in zip(s0, s1)
        for s0, s1 in zip(o1, o2)]
print(b)

def get_relative_coords(p, q):
    "from two points get the relative scanner to 0"
    distance(p, q)
    pass


# for i, d1 in enumerate(pairwise_distances):
#     for j in range(i + 1, len(pairwise_distances)):
#         print(f"{(i, j)}: {overlapping(d1.keys(), pairwise_distances[j].keys())}")
#         if i == 0 and j == 1:
#             print(set(flatten(pairwise_distances[i][k]
#                       for k in pairwise_distances[i].keys() & pairwise_distances[j].keys())).__len__())
