from itertools import combinations

nums = []
with open("day01-1.txt") as f:
    for line in f:
        nums.append(int(line))
for (i, j) in combinations(nums, 2):
    if i + j == 2020:
        print(i, j)
        print(i * j)