import copy

seats = []
with open("day11-1.txt") as f:
    for line in f:
        seats.append(list(line.strip()))

visible = {}

w = len(seats[0])
h = len(seats)

def first_nonempty(origin, direction):
    o_x, o_y = origin
    d_x, d_y = direction
    p_x = o_x + d_x
    p_y = o_y + d_y
    if p_x < 0 or p_y < 0 or p_x >= w or p_y >= h:
        return False
    while seats[p_y][p_x] == ".":
        p_x += d_x
        p_y += d_y
        if p_x < 0 or p_y < 0 or p_x >= w or p_y >= h:
            return False
    return (p_x, p_y)

# build surrounding list
for y in range(h):
    for x in range(w):
        visible[(x, y)] = []
        for d in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            if (l := first_nonempty((x, y), d)):
                visible[(x, y)].append(l)


def get_visible(s, x, y):
    l = []
    for (i, j) in visible[(x, y)]:
        l.append(s[j][i])
    return l

def iteration(s):
    n = copy.deepcopy(s)
    for y in range(h):
        for x in range(w):
            surround = get_visible(s, x, y)
            if s[y][x] == "L" and (not "#" in surround):
                n[y][x] = "#"
            elif s[y][x] == "#" and surround.count("#") >= 5:
                n[y][x] = "L"
    return n

n = iteration(seats)
while n != seats:
    seats = n.copy()
    n = iteration(seats)
tot = 0
for i in n:
    tot += i.count("#")
print(tot)
