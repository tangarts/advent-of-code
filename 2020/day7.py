import pytest
import re
from advent_of_code.core import parse_input, mapt
raw_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags"""

def get_bag_quantity(bag: str):
    n, bag = bag.split(maxsplit=1)
    if n == "no":
        n = 0 
    return bag, int(n)


def parser(line: str):
    src, dest = line.split(" bags contain ")
    dest = re.sub(r" bags?|[.]", "", dest)
    return src, list(map(get_bag_quantity, dest.split(", ")))

test_graph = dict(parse_input(raw_input, parser=parser))
day7 = dict(parse_input('data/input7.txt', parser=parser, test=False))

def part1(graph) -> int:
    def has_shiny_gold(graph, src) -> bool:
        if src == "shiny gold":
            return True
        return any(has_shiny_gold(graph, b) for b, _ in graph.get(src, []))
    return sum(1 for src in graph if has_shiny_gold(graph, src)) - 1

# print(part1(test_graph))
# print(part1(day7))

def count_bags(graph, start) -> int:
    count = 0
    for bag, quantity in graph[start]:
        count += quantity
        if quantity > 0:
            count += quantity*count_bags(graph, bag)
    return count

def test_count_bag():
    assert count_bags(test_graph, "faded blue") == 0
    assert count_bags(test_graph, "vibrant plum") == 11
    assert count_bags(test_graph, "dark olive") == 7
    assert count_bags(test_graph, "shiny gold") == 32

assert count_bags(day7, "shiny gold") == 20189

