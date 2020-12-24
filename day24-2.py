from collections import deque
from copy import deepcopy

t = []

with open("day24-1.txt") as f:
    t = [x.strip() for x in f.readlines()]


def grid(line):
    pos = [0, 0]
    l = deque(line)
    while l:
        p = l.popleft()
        if p == "e":
            pos[0] += 2
        elif p == "w":
            pos[0] -= 2
        elif p == "s":
            p = l.popleft()
            pos[1] -= 1
            if p == "e":
                pos[0] += 1
            elif p == "w":
                pos[0] -= 1
        elif p == "n":
            p = l.popleft()
            pos[1] += 1
            if p == "e":
                pos[0] += 1
            elif p == "w":
                pos[0] -= 1
    return tuple(pos)


flipped = set()
for a in t:
    p = grid(a)
    if p in flipped:
        flipped.remove(p)
    else:
        flipped.add(p)
print(len(flipped))


def black_neighbour(pos, f):
    x, y = pos
    n = [
        (x + 2, y),
        (x - 2, y),
        (x + 1, y - 1),
        (x - 1, y - 1),
        (x + 1, y + 1),
        (x - 1, y + 1),
    ]
    return len([x for x in n if x in f])


def flip(f):
    new_f = set()
    ho = [x[0] for x in f]
    x_lo = min(ho) - 2
    x_hi = max(ho) + 3
    ve = [x[1] for x in f]
    y_lo = min(ve) - 1
    y_hi = max(ve) + 2
    for x in range(x_lo, x_hi):
        for y in range(y_lo, y_hi):
            bn = black_neighbour((x,y), f)
            if (x, y) in f:
                if 0 < bn <= 2:
                    new_f.add((x, y))
            elif bn == 2:
                new_f.add((x, y))
    return new_f

for i in range(100):
    flipped = flip(flipped)
print(len(flipped))