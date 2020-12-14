def encode(num, mask):
    n = list(bin(num)[2:])
    n = ["0" for x in range(36 - len(n))] + n
    for ind, val in enumerate(mask):
        if val != "X":
            n[ind] = val
    tot = 0
    for ind, val in enumerate(reversed(n)):
        tot += int(val) * 2 ** ind
    return tot


mem = {}
mask = ""
with open("day14-1.txt") as f:
    for line in f:
        if line[:4] == "mask":
            mask = line.strip()[7:]
        elif line[:3] == "mem":
            mem[line.split(" = ")[0][4:-1]] = encode(int(line.split(" = ")[1].strip()), mask)

counter = 0
for ind, x in mem.items():
    if x != 0:
        counter += x
print(counter)
