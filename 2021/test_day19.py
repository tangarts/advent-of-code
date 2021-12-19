import pytest
from day19 import *


raw2d = """--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1"""

test2d = dict(parse_input(raw2d, sep="\n\n", parser=strip_scanner))

print(get_pairwise(test2d, 0))
print(get_pairwise(test2d, 1))


orientation3d = """--- scanner 0 ---
-1,-1,1
-2,-2,2
-3,-3,3
-2,-3,1
5,6,-4
8,0,7

--- scanner 1 ---
1,-1,1
2,-2,2
3,-3,3
2,-1,3
-5,4,-6
-8,-7,0

--- scanner 2 ---
-1,-1,-1
-2,-2,-2
-3,-3,-3
-1,-3,-2
4,6,5
-7,0,8

--- scanner 3 ---
1,1,-1
2,2,-2
3,3,-3
1,3,-2
-4,-6,5
7,0,8

--- scanner 4 ---
1,1,1
2,2,2
3,3,3
3,1,2
-6,-4,-5
0,7,-8"""

o3d =  dict(parse_input(orientation3d, sep="\n\n", parser=strip_scanner)) 

pairwise_distances = [get_pairwise(o3d, i) for i in test3d]

print([x.keys() - y.keys()for x, y in combinations(pairwise_distances, 2)])
