from itertools import product

def to_dec(n):
    tot = 0
    for ind, val in enumerate(reversed(n)):
        tot += int(val) * 2 ** ind
    return tot


def encode(num, mask):
    res = []
    n = list(bin(num)[2:])
    n = ["0" for x in range(36 - len(n))] + n
    for ind, val in enumerate(mask):
        if val == "1":
            n[ind] = "1"
    indices = [i for i, x in enumerate(mask) if x == "X"]
    for l in product("10", repeat=len(indices)):
        new = n.copy()
        for ind, val in zip(indices, l):
            new[ind] = val
        res.append(to_dec(new))
    return res


mem = {}
mask = ""
with open("day14-1.txt") as f:
    for line in f:
        if line[:4] == "mask":
            mask = line.strip()[7:]
        elif line[:3] == "mem":
            locs = encode(int(line.split(" = ")[0][4:-1]), mask)
            for l in locs:
                mem[l] = int(line.split(" = ")[1].strip())

counter = 0
for ind, x in mem.items():
    if x != 0:
        counter += x
print(counter)
