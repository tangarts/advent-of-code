#%%

raw = """939
7,13,x,x,59,x,31,19"""


def parse_timetable(_input):
    bus, ids = _input.split("\n")
    bus = int(bus)
    ids = [int(s) for s in ids.split(",") if s != "x"]
    return bus, ids


def part1(bus, ids):
    def earliest_bus(bus, ids):
        b = bus
        while True:
            for i in ids:
                if (b % i) == 0:
                    return b, i
            b += 1

    earliest, bus_id = earliest_bus(bus, ids)
    return bus_id * (earliest - bus)


test_bus, test_ids = parse_timetable(raw)
assert part1(test_bus, test_ids) == 295

with open("data/input13.txt") as f:
    data = f.read().rstrip()
    print(data)
    bus, ids = parse_timetable(data)

assert part1(bus, ids) == 161
