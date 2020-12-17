from itertools import product

active = set()

with open("day17-1.txt") as f:
    for i, line in enumerate(f):
        for j, cube in enumerate(line.strip()):
            if cube == "#":
                active.add((j, i, 0, 0))

x, y, z, w = (-1, j + 2), (-1, i + 2), (-1, 0 + 2), (-1, 0 + 2)


def get_neighbour(i, j, k, l):
    n = [
        (a, b, c, d)
        for a in range(i - 1, i + 2)
        for b in range(j - 1, j + 2)
        for c in range(k - 1, k + 2)
        for d in range(l - 1, l + 2)
    ]
    n.remove((i, j, k, l))
    return n


def is_active(i, j, k, l):
    active_neighbour = sum([coord in active for coord in get_neighbour(i, j, k, l)])
    if (i, j, k, l) in active:
        return active_neighbour in [2, 3]
    else:
        return active_neighbour == 3


def cycle(active):
    new_active = set()
    for i, j, k, l in product(range(*x), range(*y), range(*z), range(*w)):
        if is_active(i, j, k, l):
            new_active.add((i, j, k, l))
    return new_active


def update_xyz(active):
    # update x, y, z
    t = [a[0] for a in active]
    x = (min(t) - 1, max(t) + 2)
    t = [a[1] for a in active]
    y = (min(t) - 1, max(t) + 2)
    t = [a[2] for a in active]
    z = (min(t) - 1, max(t) + 2)
    t = [a[3] for a in active]
    w = (min(t) - 1, max(t) + 2)
    return x, y, z, w


for i in range(6):
    active = cycle(active)
    x, y, z, w = update_xyz(active)
print(len(active))
