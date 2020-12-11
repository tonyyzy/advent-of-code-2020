import copy

seats = []
with open("day11-1.txt") as f:
    for line in f:
        seats.append(list(line.strip()))


def iteration(s):
    new = copy.deepcopy(s)
    w = len(s[0]) - 1
    h = len(s) - 1
    # corners
    if s[0][0] == "L" and not "#" in [s[0][1], s[1][1], s[1][0]]:
        new[0][0] = "#"
    if s[0][w] == "L" and not "#" in [s[0][w - 1], s[1][w], s[1][w - 1]]:
        new[0][w] = "#"
    if s[h][0] == "L" and not "#" in [s[h - 1][0], s[h - 1][1], s[h][1]]:
        new[h][0] = "#"
    if s[h][w] == "L" and not "#" in [s[h - 1][w - 1], s[h - 1][w], s[h][w - 1]]:
        new[h][w] = "#"

    # edges
    for x in range(1, w):
        surround = [s[0][x - 1], s[0][x + 1], s[1][x - 1], s[1][x], s[1][x + 1]]
        if s[0][x] == "L" and not "#" in surround:
            new[0][x] = "#"
        elif s[0][x] == "#" and surround.count("#") >= 4:
            new[0][x] = "L"
    for x in range(1, w):
        surround = [
            s[h][x - 1],
            s[h][x + 1],
            s[h - 1][x - 1],
            s[h - 1][x],
            s[h - 1][x + 1],
        ]
        if s[h][x] == "L" and not "#" in surround:
            new[h][x] = "#"
        elif s[h][x] == "#" and surround.count("#") >= 4:
            new[h][x] = "L"
    for y in range(1, h):
        surround = [s[y - 1][0], s[y + 1][0], s[y - 1][1], s[y][1], s[y + 1][1]]
        if s[y][0] == "L" and not "#" in surround:
            new[y][0] = "#"
        elif s[y][0] == "#" and surround.count("#") >= 4:
            new[y][0] = "L"
    for y in range(1, h):
        surround = [
            s[y - 1][w],
            s[y + 1][w],
            s[y - 1][w - 1],
            s[y][w - 1],
            s[y + 1][w - 1],
        ]
        if s[y][w] == "L" and not "#" in surround:
            new[y][w] = "#"
        elif s[y][w] == "#" and surround.count("#") >= 4:
            new[y][w] = "L"

    for y in range(1, h):
        for x in range(1, w):
            surround = [
                s[y - 1][x],
                s[y + 1][x],
                s[y - 1][x - 1],
                s[y][x - 1],
                s[y + 1][x - 1],
                s[y - 1][x + 1],
                s[y][x + 1],
                s[y + 1][x + 1],
            ]
            if s[y][x] == "L" and not "#" in surround:

                new[y][x] = "#"
            elif s[y][x] == "#" and surround.count("#") >= 4:
                new[y][x] = "L"
    return new

# for i in seats:
#     print("".join(i))
n = iteration(seats)
# for i in n:
#     print("".join(i))
while n != seats:
    seats = n.copy()
    n = iteration(seats)
tot = 0
for i in n:
    tot += i.count("#")
print(tot)