with open("day22-1.txt") as f:
    p1, p2 =  f.read().split("\n\n")
    p1 = [int(x) for x in p1.splitlines()[1:]]
    p2 = [int(x) for x in p2.splitlines()[1:]]

while len(p1) != 0 and len(p2) != 0:
    if p1[0] > p2[0]:
        p1 = p1[1:] + [p1[0], p2[0]]
        p2 = p2[1:]
    elif p1[0] < p2[0]:
        p2 = p2[1:] + [p2[0], p1[0]]
        p1 = p1[1:]

counter = 0
if len(p1) > 0:
    for i, j in enumerate(reversed(p1)):
        counter += (i + 1) * j
print(counter)