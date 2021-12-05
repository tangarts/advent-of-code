from advent_of_code.core import *

passport = data("2020/data/input_4.txt", sep="\n\n", test=False)

test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

test_input = data(test_input, sep="\n\n")

codes = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # "cid")

# %%
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
