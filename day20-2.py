from itertools import product, permutations
from copy import deepcopy
import re

tiles = {}

image = [
    ("2221", 1, "tb"),
    ("2309", 0, "tb"),
    ("2381", 0, None),
    ("3191", 3, None),
    ("1997", 0, None),
    ("3449", 3, None),
    ("1669", 2, None),
    ("3947", 3, None),
    ("1237", 2, None),
    ("3407", 2, None),
    ("2399", 2, None),
    ("2753", 3, "lr"),
    ("1307", 2, None),
    ("2677", 1, "lr"),
    ("3643", 1, "lr"),
    ("3461", 1, "tb"),
    ("1187", 3, "lr"),
    ("1721", 3, None),
    ("1597", 0, None),
    ("3917", 2, None),
    ("1097", 1, "tb"),
    ("2137", 1, None),
    ("3361", 0, "tb"),
    ("1613", 1, None),
    ("1019", 1, None),
    ("3001", 3, None),
    ("2803", 1, "lr"),
    ("2203", 0, None),
    ("2113", 1, "tb"),
    ("2939", 3, None),
    ("2237", 0, None),
    ("2281", 2, "lr"),
    ("1129", 3, "tb"),
    ("1201", 0, None),
    ("3529", 1, None),
    ("1321", 1, "lr"),
    ("1567", 0, None),
    ("3739", 0, None),
    ("2377", 1, None),
    ("2131", 1, None),
    ("2851", 1, "tb"),
    ("2657", 1, "lr"),
    ("1637", 1, "tb"),
    ("2693", 3, "lr"),
    ("1447", 1, "tb"),
    ("1163", 3, None),
    ("2239", 0, None),
    ("2087", 3, None),
    ("2069", 1, None),
    ("3709", 0, None),
    ("2539", 1, None),
    ("1381", 3, None),
    ("2161", 1, "lr"),
    ("3299", 1, None),
    ("1087", 0, "tb"),
    ("1123", 3, None),
    ("1823", 1, "tb"),
    ("1171", 1, None),
    ("3251", 3, None),
    ("3373", 0, None),
    ("3793", 1, "lr"),
    ("3881", 0, None),
    ("1181", 0, "tb"),
    ("1987", 0, None),
    ("3061", 1, None),
    ("2711", 1, "lr"),
    ("1847", 1, None),
    ("2903", 3, "tb"),
    ("3593", 1, "lr"),
    ("1433", 2, None),
    ("2957", 0, "tb"),
    ("1801", 3, "lr"),
    ("3229", 2, None),
    ("1061", 0, "tb"),
    ("3833", 1, "lr"),
    ("2833", 0, "tb"),
    ("1873", 3, None),
    ("2251", 0, None),
    ("3853", 2, None),
    ("3067", 3, "tb"),
    ("2467", 2, None),
    ("2027", 1, "lr"),
    ("3631", 0, None),
    ("1051", 1, None),
    ("2837", 2, "lr"),
    ("3049", 3, "tb"),
    ("3637", 3, None),
    ("2659", 3, "tb"),
    ("3613", 0, None),
    ("1153", 2, None),
    ("2897", 1, "tb"),
    ("2617", 3, None),
    ("2083", 1, "tb"),
    ("3163", 0, None),
    ("3697", 2, None),
    ("1223", 3, "lr"),
    ("3467", 0, None),
    ("2687", 0, None),
    ("2593", 3, "lr"),
    ("3469", 1, "lr"),
    ("3797", 1, None),
    ("1373", 2, None),
    ("1091", 3, "tb"),
    ("2273", 3, "tb"),
    ("2819", 0, "tb"),
    ("3607", 1, "tb"),
    ("3863", 1, None),
    ("3089", 1, "tb"),
    ("3041", 3, "tb"),
    ("3989", 3, None),
    ("2843", 0, None),
    ("2389", 3, "tb"),
    ("2861", 3, None),
    ("2293", 0, None),
    ("1291", 0, None),
    ("3319", 2, None),
    ("1483", 0, None),
    ("3517", 3, None),
    ("3533", 0, "tb"),
    ("3499", 0, None),
    ("2333", 1, None),
    ("3019", 0, None),
    ("1063", 1, "lr"),
    ("3259", 1, "lr"),
    ("3617", 0, None),
    ("2411", 3, None),
    ("3343", 1, "lr"),
    ("1951", 0, None),
    ("1931", 3, "lr"),
    ("1069", 1, None),
    ("3929", 3, "tb"),
    ("3371", 0, None),
    ("1559", 0, "tb"),
    ("1259", 0, "tb"),
    ("1471", 2, "lr"),
    ("1487", 2, None),
    ("3203", 0, "tb"),
    ("3331", 1, None),
    ("3761", 3, None),
    ("1831", 2, None),
    ("3079", 2, None),
    ("2699", 3, None),
    ("2543", 3, None),
    ("3011", 2, "lr"),
]

# image = [
#     ("1951", 0, "tb"),
#     ("2311", 0, "tb"),
#     ("2729", 0, "tb"),
#     ("3079", 0, None),
#     ("1427", 2, "lr"),
#     ("2971", 0, "tb"),
#     ("2473", 1, "tb"),
#     ("1489", 0, "tb"),
#     ("1171", 2, "tb"),
# ]

with open("day20-1.txt") as f:
    for tile in f.read().split("\n\n"):
        grid = []
        lines = tile.splitlines()
        num = lines[0][-5:-1]
        for line in lines[1:]:
            grid.append(list(line))
        tiles[num] = grid

# print(len(tiles))


def rot_flip(r, f, g):
    for i in range(r):
        new_g = []
        for line in range(len(g)):
            new_g.append([x[line] for x in reversed(g)])
        g = new_g

    new_g = []
    if f == "lr":
        for line in g:
            new_g.append(list(reversed(line)))
        g = new_g
    new_g = []
    if f == "tb":
        for line in reversed(g):
            new_g.append(list(line))
            g = new_g

    return g


def pg(g):
    for l in g:
        print("".join(l))


MAX = int(len(tiles) ** 0.5) - 1


def next_tile(pos):
    x, y = pos
    if x == 0 and y != MAX:
        return (y + 1, x)
    elif x == MAX and y == MAX:
        return None
    elif y == MAX:
        return (y, x + 1)
    else:
        return (x - 1, y + 1)


nt = (0, 0)
counter = 0
order = {nt: 0}
while nt:
    order[nt] = counter
    counter += 1
    nt = next_tile(nt)

grid = [[[] for j in range(MAX + 1)] for i in range(MAX + 1)]
# print(order)

for k, v in order.items():
    t, rot, flip = image[v]
    grid[k[1]][k[0]] = rot_flip(rot, flip, tiles[t])


def monster_count(g):
    l = len(g)
    counter = 0
    x = 2
    y = 2
    # print(
    #     g[y][x + 18],
    #     g[y + 1][x],
    #     g[y + 1][x + 5 : x + 7],
    #     g[y + 1][x + 11 : x + 13]
    #     # and g[y + 1][x + 17 : x + 20] == "###"
    # )
    for y in range(l - 2):
        for x in range(l - 19):
            if (
                    g[y][x + 18] == "#"
                and g[y + 1][x] == "#"
                and g[y + 1][x + 5 : x + 7] == "##"
                and g[y + 1][x + 11 : x + 13] == "##"
                and g[y + 1][x + 17 : x + 20] == "###"
                and g[y + 2][x + 1] == "#"
                and g[y + 2][x + 4] == "#"
                and g[y + 2][x + 7] == "#"
                and g[y + 2][x + 10] == "#"
                and g[y + 2][x + 13] == "#"
                and g[y + 2][x + 16] == "#"
            ):
                counter += 1

    return counter


new_grid = []

for i in range(MAX + 1):
    for j in range(1, 9):
        new_grid.append("".join(["".join(grid[i][x][j][1:9]) for x in range(MAX + 1)]))
grid = new_grid
for rot, flip in product(range(4), [None, "lr", "tb"]):
    g = rot_flip(rot, flip, grid)
    board = []

    board = ["".join(x) for x in g]
    print(sum([x.count("#") for x in board]) - monster_count(board) * 15)