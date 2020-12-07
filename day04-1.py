def validator(passport):
    fields = []
    north_pole = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    valid_passport = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
    for line in passport.split("\n"):
        for entry in line.split(" "):
            fields.append(entry.split(":")[0])
    if set(fields) == valid_passport or set(fields) == north_pole:
        return True

with open("day04-1.txt") as f:
    counter = 0
    for passport in f.read().split("\n\n"):
        if validator(passport):
            counter += 1
    print(counter)