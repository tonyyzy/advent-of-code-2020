from itertools import combinations

nums = []
with open("day01-1.txt") as f:
    for line in f:
        nums.append(int(line))
for i in combinations(nums, 3):
    if sum(i) == 2020:
        print(i)
        print(i[0] * i[1] * i[2])