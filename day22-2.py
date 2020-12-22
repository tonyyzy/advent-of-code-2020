with open("day22-1.txt") as f:
    p1, p2 =  f.read().split("\n\n")
    p1 = [int(x) for x in p1.splitlines()[1:]]
    p2 = [int(x) for x in p2.splitlines()[1:]]

# p1 = [9, 2, 6, 3, 1]
# p2 = [5, 8, 4, 7, 10]

c = 0
def rec(p1, p2):
    p = set()
    global c
    c += 1
    cc = c
    r = 1
    # print("game", cc)
    while len(p1) != 0 and len(p2) != 0:
        # print("round", r, "game", cc)
        r += 1
        # print(p1)
        # print(p2)
        if (tuple(p1), tuple(p2)) in p:
            # print("yes")
            # print(p1, p2)
            p1 = p1[1:] + [p1[0], p2[0]]
            p2 = p2[1:]
            return "p1", p1, p2
        else:
            p.add((tuple(p1), tuple(p2)))
            if p1[0] < len(p1) and p2[0] < len(p2):
                res = rec(p1[1:p1[0] + 1], p2[1:p2[0] + 1])
                # print("game", cc)

                if res[0] == "p1":
                    p1 = p1[1:] + [p1[0], p2[0]]
                    p2 = p2[1:]
                else:
                    p2 = p2[1:] + [p2[0], p1[0]]
                    p1 = p1[1:]
            else:
                # print("hey")
                if p1[0] > p2[0]:
                    p1 = p1[1:] + [p1[0], p2[0]]
                    p2 = p2[1:]
                elif p1[0] < p2[0]:
                    # print(p1[0], p2[0])
                    p2 = p2[1:] + [p2[0], p1[0]]
                    p1 = p1[1:]
                    # print(p1, p2)
    if len(p1) == 0:
        return "p2", p1, p2
    else:
        return "p1", p1, p2

_, p1, p2 = rec(p1, p2)
# _, p1, p2 = rec([3], [9, 7, 5, 4, 1, 10, 8])
counter = 0
print(p1, p2)
# if len(p1) > 0:
for i, j in enumerate(reversed(p1)):
    counter += (i + 1) * j
print(counter)