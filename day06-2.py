from collections import Counter

total = 0
with open("day06-1.txt") as f:
    for group in f.read().strip().split("\n\n"):
        people = group.count("\n") + 1
        for i, j in Counter(group).most_common():
            if j == people:
                total += 1
    print(total)
