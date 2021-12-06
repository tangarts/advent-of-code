from advent_of_code.core import *

parser = lambda s: s.replace("\n", " ").split(" ")

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

test_input = data(_test_input, sep="\n\n")

codes = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

# %%

passport = data("2020/data/input_4.txt", sep="\n\n", test=False)
assert quantify(test_input, lambda col: all(c in col for c in codes)) == 2
assert quantify(passport, lambda col: all(c in col for c in codes)) == 260


# * byr (Birth Year) - four digits; at least 1920 and at most 2002.
# * iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# * eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# * hgt (Height) - a number followed by either cm or in:
# * If cm, the number must be at least 150 and at most 193.
# * If in, the number must be at least 59 and at most 76.
# * hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# * ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# * pid (Passport ID) - a nine-digit number, including leading zeroes.
# * cid (Country ID) - ignored, missing or not.

test_input2 = mapt(parser, test_input)

str_to_dict = lambda col: dict([tuple(s.split(":")) for s in col])
test_input2 = [str_to_dict(passport) for passport in test_input2]

def isvalid(v) -> dict:
    rules = {
    'byr' : "1920" <= v <= "2002",
    'iyr' : "2020" <= v <= "2020",
    'eyr' : "2020" <= v <= "2030",
    'hgt' : ((v.endswith('cm') and "150" <= v <= "193") or
             (v.endswith('in') and "59" <= v <= "76")),
    'hcl' : first(v) == "#" and 
            all(cl in "0123456789abcdef" for cl in v[1:]) and 
            len(v) == 6,
    'ecl' : v in ('amb', 'blu', 'brn', 'gry', 'hzl', 'oth'),
    'pid' : len(v) == 9 and set(v) == set(str(x) for x in range(10)),
    }
    return rules

def valid_passport(passport):
    return (all(c in codes for c in passport))
