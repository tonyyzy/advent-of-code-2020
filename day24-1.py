from collections import deque    
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
            p =l.popleft()
            if p == "e":
                pos[0] += 1
                pos[1] -= 1
            elif p == "w":
                pos[0] -= 1
                pos[1] -= 1
        elif p == "n":
            p =l.popleft()
            if p == "e":
                pos[0] += 1
                pos[1] += 1
            elif p == "w":
                pos[0] -= 1
                pos[1] += 1
    return tuple(pos)

flipped = set()
for a in t:
    p = grid(a)
    if p in flipped:
        flipped.remove(p)
    else:
        flipped.add(p)
print(len(flipped))