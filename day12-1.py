facing = "E"
loc = {"N": 0, "S": 0, "E": 0, "W": 0}
with open("day12-1.txt") as f:
    for line in f:
        l = line[0]
        n = int(line.strip()[1:])
        if l == "F":
            loc[facing] += n
        elif l in "NSEW":
            loc[l] += n
        elif l == "L":
            facing = "NWSE"[int(((n / 90) + "NWSE".index(facing)) % 4)]
        elif l == "R":
            facing = "NESW"[int(((n / 90) + "NESW".index(facing)) % 4)]

# print(loc)
print(abs(loc["N"]  - loc["S"]) + abs(loc["W"]  - loc["E"]))
