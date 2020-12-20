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
cases = set(construct("0"))
# print(cases)
counter = 0
for l in inp.split("\n"):
    if l.strip() in cases:
        counter += 1

print(counter)

        
