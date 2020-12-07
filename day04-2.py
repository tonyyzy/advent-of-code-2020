import re

def validator(passport):
    fields = []
    north_pole = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    # valid_passport = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
    for line in passport.split("\n"):
        for entry in line.split(" "):
            try:
                key, value = entry.split(":")
            except:
                print(entry)
            if key == "byr" and 1920 <= int(value) <= 2002:
                fields.append(key)
            if key == "iyr" and 2010 <= int(value) <= 2020:
                fields.append(key)
            if key == "eyr" and 2020 <= int(value) <= 2030:
                fields.append(key)
            if key == "hgt":
                if value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193:
                    fields.append(key)
                elif value[-2:] == "in" and 59 <= int(value[:-2]) <= 76:
                    fields.append(key)
            if key == "hcl" and re.search(r'^#(?:[0-9a-f]{6})$', value):
                fields.append(key)
            if key == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                fields.append(key)
            if key == "pid" and len(value) == 9 and value.isnumeric():
                fields.append(key)
    if set(fields) == north_pole:
        return True

with open("day04-1.txt") as f:
    counter = 0
    for passport in f.read().split("\n\n"):
        if validator(passport):
            counter += 1
    print(counter)