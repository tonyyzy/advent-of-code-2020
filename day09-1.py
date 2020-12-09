from itertools import combinations

nums = []
with open("day09-1.txt") as f:
    for line in f:
        nums.append(int(line.strip()))

def check(l, num):
    sums = [x + y for x, y in combinations(l, 2)]
    return num in sums

for i in range(25, len(nums)):
    if not check(nums[i-25:i], nums[i]):
        print(nums[i])