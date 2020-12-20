rules = {}
from itertools import product

with open("day19-1.txt") as f:
    r, inp = f.read().split("\n\n")

for line in r.split("\n"):
    ind, rule = line.strip().split(":")
    if "\"" in rule:
        rules[ind] = rule.strip().replace("\"", "")
    else:
        rules[ind] = [[x for x in rulez.strip().split(" ")] for rulez in rule.split("|")]

# construct possible cases
pos = '0'
cases = set()
def construct(pos):
    if type(r := rules[pos]) == str:
        return [r]
    elif len(r) == 2:
        return ["".join(x) for x in product(*[construct(x) for x in r[0]])] + ["".join(x) for x in product(*[construct(x) for x in r[1]])]
    else:
        return ["".join(x) for x in product(*[construct(x) for x in r[0]])]
c42 = set(construct("42"))
c31 = set(construct("31"))

#42(x+y) + 31y
unit = [len(x) for x in c31][0]
def checker(s):
    c42c = 0
    c31c = 0
    while s[:unit] in c42:
        c42c += 1
        s = s[unit:]
    while s[:unit] in c31:
        c31c += 1
        s = s[unit:]
    if c42c == 0 or c31c == 0 or len(s) > 0:
        return False
    elif c42c - c31c > 0:
        return True
    return False

inp = inp.split("\n")
counter = 0
for i in inp:
    if checker(i):
        counter += 1
print(counter)