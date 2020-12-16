rules = {}


def validator(nums, rules):
    res = []
    for num in nums:
        if not any(
            [
                (l1 <= num <= h1) or (l2 <= num <= h2)
                for ((l1, h1), (l2, h2)) in rules.values()
            ]
        ):
            res.append(num)
    return res


def map(nums, rules):
    for i, num in enumerate(nums):
        for k, ((l1, h1), (l2, h2)) in rules.items():
            if not ((l1 <= num <= h1) or (l2 <= num <= h2)):
                exclude[k].append(i)


with open("day16-1.txt") as f:
    rule, ticket, nearby = f.read().split("\n\n")
    for line in rule.split("\n"):
        parts = line.strip().split(" ")
        l1, h1 = parts[-3].split("-")
        l2, h2 = parts[-1].split("-")
        rules[line.split(":")[0]] = ((int(l1), int(h1)), (int(l2), int(h2)))
    tot = 0
    valid = []
    for line in nearby.split("\n")[1:]:
        l = [int(x) for x in line.split(",")]
        if not (c := validator(l, rules)):
            valid.append(l)
        for i in c:
            tot += i
exclude = {x: [] for x in rules.keys()}
pos = set(range(len(rules)))
# print(len(valid))
for v in valid:
    map(v, rules)
exclude = dict(sorted(exclude.items(), key=lambda x: len(x[1]), reverse=True))
print(exclude)
res = []
for k, v in exclude.items():
    p = pos - set(v)
    pos = set(v)
    if "departure" in  k:
        res.append(p.pop())
ticket = [int(x) for x in ticket.split("\n")[1].split(",")]
e = 1
for i in [ticket[x] for x in res]:
    e *= i
print(e)

# print(tot)
# print(rules)
