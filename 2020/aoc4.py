# %%
with open("data/.txt") as f:
    data = f.read()
# %%
passport = [line for line in data.split("\n\n")]
print(passport)
# %%


codes = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # "cid")

# %%
number_not_valid = 0
for docs in passport:
    not_valid = False
    for c in codes:
        if c not in docs:
            not_valid = True
    if not_valid:
        number_not_valid += 1

len(passport) - number_not_valid


"""
* byr (Birth Year) - four digits; at least 1920 and at most 2002.
* iyr (Issue Year) - four digits; at least 2010 and at most 2020.
* eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
* hgt (Height) - a number followed by either cm or in:
* If cm, the number must be at least 150 and at most 193.
* If in, the number must be at least 59 and at most 76.
* hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
* ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
* pid (Passport ID) - a nine-digit number, including leading zeroes.
* cid (Country ID) - ignored, missing or not.

"""
