from itertools import product, permutations
from copy import deepcopy

tiles = {}

with open("day20-test.txt") as f:
    for tile in f.read().split("\n\n"):
        grid = []
        lines = tile.splitlines()
        num = lines[0][-5:-1]
        for line in lines[1:]:
            grid.append(list(line))
        tiles[num] = grid

def get_edges(g):
    top = "".join(g[0])
    bottom = "".join(g[-1])
    left = "".join([x[0] for x in g])
    right = "".join([x[-1] for x in g])
    return top, bottom, left, right


def rot_flip(r, f, g):
    for i in range(r):
        new_g = []
        for line in range(10):
            new_g.append([x[line] for x in reversed(g)])
        g = new_g

    new_g = []
    if f == "lr":
        for line in g:
            new_g.append(list(reversed(line)))
        g = new_g

    if f == "tb":
        g = list(reversed(g))

    return g


def pg(g):
    for l in g:
        print("".join(l))

# rot 0, 1, 2, 3, flip None || lr || tb
top = {}
bottom = {}
left = {}
right = {}
for k, v in tiles.items():
    e = []
    for rot, flip in product(range(4), [None, "lr", "tb"]):
        t, b, l, r = get_edges(rot_flip(rot, flip, v))
        if t not in top.keys():
            top[t] = []
        if b not in bottom.keys():
            bottom[b] = []
        if l not in left.keys():
            left[l] = []
        if r not in right.keys():
            right[r] = []
        top[t].append((k, rot, flip))
        bottom[b].append((k, rot, flip))
        left[l].append((k, rot, flip))
        right[r].append((k, rot, flip))

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

print(order)

def checker(pos, choices, grid, arr):
    # print(grid)
    x, y = pos
    # print(pos)
    nt = next_tile(pos)

    if y == 0:
        left_tile = grid[order[(x - 1, y)]]
        left_constraint = arr[(x - 1, y)]["r"]
        possible = [x for x in left[left_constraint] if x[0] in choices]
    elif x == 0:
        top_tile = grid[order[(x, y - 1)]]
        top_constraint = arr[(x, y - 1)]["b"]
        possible = [x for x in top[top_constraint] if x[0] in choices]
    else:
        left_tile = grid[order[(x - 1, y)]]
        left_constraint = arr[(x - 1, y)]["r"]
        left_possible = set([x for x in left[left_constraint] if x[0] in choices])
        top_tile = grid[order[(x, y - 1)]]
        top_constraint = arr[(x, y - 1)]["b"]
        top_possible = set([x for x in top[top_constraint] if x[0] in choices])
        possible = left_possible.intersection(top_possible)

    # print(possible)
    if len(possible) > 0:
        if nt == None:
            print(grid)
            print(possible)
            print(
                int(grid[order[(0, 0)]])
                * int(grid[order[(MAX, 0)]])
                * int(grid[order[(0, MAX)]])
                * int(list(possible)[0][0])
            )
            return True
        res = []
        for p in possible:
            a = deepcopy(arr)
            t, b, l, r = get_edges(rot_flip(p[1], p[2], tiles[p[0]]))
            a[pos]["b"] = b
            a[pos]["r"] = r
            if checker(nt, [x for x in choices if x != p[0]], grid + [p], a):
                return True
            else:
                break
        # print(res)
        return False

    else:
        return False


# start pick one for (0, 0)
tis = list(tiles.keys())
for start in tis:
    pos = (0, 0)
    for rot, flip in product(range(4), [None, "lr", "tb"]):
        grid = [(start, rot, flip)]
        arr = {(x, y): {"b": "", "r": ""} for x in range(MAX+1) for y in range(MAX+1)}
        t, b, l, r = get_edges(rot_flip(rot, flip, tiles[grid[0][0]]))
        # arr[(0, 0)]["t"] = t
        arr[(0, 0)]["b"] = b
        # arr[(0, 0)]["l"] = l
        arr[(0, 0)]["r"] = r
        checker((1, 0), [x for x in tis if x != start], grid, arr)
# grid = ["3709"]
# arr = {(x, y): {"b": "", "r": ""} for x in range(MAX+1) for y in range(MAX+1)}
# t, b, l, r = get_edges(tiles[grid[0]])
# # arr[(0, 0)]["t"] = t
# arr[(0, 0)]["b"] = b
# # arr[(0, 0)]["l"] = l
# arr[(0, 0)]["r"] = r
# checker((1, 0), [x for x in tis if x != "3709"], grid, arr)
# grid = {(x, y): 0 for x in range(3) for y in range(3)}
# grid[(0, 0)] = "1951"
# arr = {
#     (x, y): {"b": "", "r": ""} for x in range(3) for y in range(3)
# }
# t, b, l, r = get_edges(rot_flip(0, "tb", tiles[grid[(0, 0)]]))
# # arr[(0, 0)]["t"] = t
# arr[(0, 0)]["b"] = b
# # arr[(0, 0)]["l"] = l
# arr[(0, 0)]["r"] = r
# print(checker((1, 0), [x for x in tis if x != "1951"], grid, arr))