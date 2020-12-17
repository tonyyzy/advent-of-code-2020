from itertools import product

active = set()


def print_layer(g):
    for line in g:
        print("".join(line))


with open("day17-1.txt") as f:
    for i, line in enumerate(f):
        for j, cube in enumerate(line.strip()):
            if cube == "#":
                active.add((j, i, 0))

x, y, z = (-1, j + 2), (-1, i + 2), (-1, 0 + 2)


def get_neighbour(i, j, k):
    return [
        (a, b, c)
        for a in range(i - 1, i + 2)
        for b in range(j - 1, j + 2)
        for c in [k - 1, k + 1]
    ] + [
        (a, b, k)
        for a in range(i - 1, i + 2)
        for b in range(j - 1, j + 2)
        if (a != i or b != j)
    ]


def is_active(i, j, k):
    active_neighbour = sum([coord in active for coord in get_neighbour(i, j, k)])
    if (i, j, k) in active:
        return active_neighbour in [2, 3]
    else:
        return active_neighbour == 3


def cycle(active):
    new_active = set()
    for i, j, k in product(range(*x), range(*y), range(*z)):
        if is_active(i, j, k):
            new_active.add((i, j, k))
    return new_active


def update_xyz(active):
    # update x, y, z
    t = [a[0] for a in active]
    x = (min(t) - 1, max(t) + 2)
    t = [a[1] for a in active]
    y = (min(t) - 1, max(t) + 2)
    t = [a[2] for a in active]
    z = (min(t) - 1, max(t) + 2)
    return x, y, z


for i in range(6):
    active = cycle(active)
    x, y, z = update_xyz(active)
print(len(active))
