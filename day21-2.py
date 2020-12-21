a = {}
ft = []
with open("day21-1.txt") as f:
    for line in f:
        food, allergens = line.split("(")
        food, allergens = food.strip().split(" "), allergens.strip()[9:-1].split(", ")
        ft += food
        for allergen in allergens:
            if allergen not in a.keys():
                a[allergen] = set(food)
            else:
                a[allergen] = a[allergen].intersection(set(food))
na = set(ft) - set([y for x in a.values() for y in x])
print(len([x for x in ft if x in na]))
known = set()
res = {}
while max([len(x) for x in a.values()]) > 1:
    for k, v in sorted(a.items(), key=lambda x: len(x[1])):
        if len(a[k]) == 1:
            known = known.union(a[k])
        else:
            a[k] = a[k] - known
print(",".join([list(a[k])[0] for k in sorted(a.keys())]))
