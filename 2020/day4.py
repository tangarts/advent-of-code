from advent_of_code.core import parse_input, quantify,mapt, first


def parser(s): return s.replace("\n", " ").split(" ")


_test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

test_input = parse_input(_test_input, sep="\n\n")

codes = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

# %%

passports = parse_input("data/input_4.txt", sep="\n\n", test=False)
assert quantify(test_input, lambda col: all(c in col for c in codes)) == 2
assert quantify(passports, lambda col: all(c in col for c in codes)) == 260

# Part 2


def str_to_dict(col) -> dict: return dict(tuple(s.split(":")) for s in col)


test_input2 = mapt(lambda s: str_to_dict(parser(s)), test_input)


def isvalid() -> dict:
    rules = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'hgt': lambda v: ((v.endswith('cm') and 150 <= int(v[:-2]) <= 193) or
                          (v.endswith('in') and 59 <= int(v[:-2]) <= 76)),
        'hcl': lambda v: first(v) == "#" and all(cl in "0123456789abcdef" for cl in v[1:]) and len(v) == 7,
        'ecl': lambda v: any(v == ecl for ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}),
        'pid': lambda v: len(v) == 9 and set(v) & set(str(x) for x in range(10)),
    }
    return rules


def valid_passport(passport: dict) -> bool:
    return (codes.issubset(passport) and all(isvalid()[key](passport[key]) for key in codes))


print(quantify(test_input2, valid_passport))
print(quantify(mapt(lambda s: str_to_dict(parser(s)), passports), valid_passport))
