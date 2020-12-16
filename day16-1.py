rules = []

def validator(nums, rules):
    res = []
    for num in nums:
        if not any([(l1 <= num <= h1) or (l2 <= num <= h2) for ((l1, h1), (l2, h2)) in rules]):
            res.append(num)
    return res

with open("day16-1.txt") as f:
    rule, ticket, nearby = f.read().split("\n\n")
    for line in rule.split("\n"):
        parts = line.strip().split(" ")
        l1,h1 = parts[-3].split("-")
        l2,h2 = parts[-1].split("-")
        rules.append(((int(l1), int(h1)), (int(l2), int(h2))))
    tot = 0
    for line in nearby.split("\n")[1:]:
        for i in validator([int(x) for x in line.split(",")], rules):
            tot += i
print(tot)
# print(rules)

