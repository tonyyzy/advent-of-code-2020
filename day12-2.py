loc = {"N": 0, "S": 0, "E": 0, "W": 0}
waypoint = {"N": 1, "S": 0, "E": 10, "W": 0}
with open("day12-1.txt") as f:
    for line in f:
        l = line[0]
        n = int(line.strip()[1:])
        if l == "F":
            for d in "NSWE":
                loc[d] += n * waypoint[d]
        elif l in "NSEW":
            waypoint[l] += n
        elif l == "L":
            for i in range(int(n/90)):
                waypoint["E"], waypoint["S"], waypoint["W"], waypoint["N"] = waypoint["S"], waypoint["W"], waypoint["N"], waypoint["E"]
        elif l == "R":
            for i in range(int(n/90)):
                waypoint["E"], waypoint["S"], waypoint["W"], waypoint["N"] = waypoint["N"], waypoint["E"], waypoint["S"], waypoint["W"]

# print(loc)
print(abs(loc["N"]  - loc["S"]) + abs(loc["W"]  - loc["E"]))
