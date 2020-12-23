with open("day22-1.txt") as f:
    p1, p2 = f.read().split("\n\n")
    p1 = [int(x) for x in p1.splitlines()[1:]]
    p2 = [int(x) for x in p2.splitlines()[1:]]

# p1 = [9, 2, 6, 3, 1]
# p2 = [5, 8, 4, 7, 10]


def rec(p1, p2):
    p = set()
    while len(p1) != 0 and len(p2) != 0:
        win = "p1"
        if (tuple(p1), tuple(p2)) in p:
            p1 = p1[1:] + [p1[0], p2[0]]
            p2 = p2[1:]
            return "p1", p1
        else:
            p.add((tuple(p1), tuple(p2)))
            if p1[0] < len(p1) and p2[0] < len(p2):
                (win, _) = rec(p1[1 : p1[0] + 1], p2[1 : p2[0] + 1])
            elif p1[0] < p2[0]:
                win = "p2"
        if win == "p1":
            p1 = p1[1:] + [p1[0], p2[0]]
            p2 = p2[1:]
        else:
            p2 = p2[1:] + [p2[0], p1[0]]
            p1 = p1[1:]
    if len(p1) == 0:
        return "p2", p2
    else:
        return "p1", p1


_, p = rec(p1, p2)
counter = 0
for i, j in enumerate(reversed(p)):
    counter += (i + 1) * j
print(counter)