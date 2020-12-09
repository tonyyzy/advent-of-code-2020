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
        invalid = nums[i]
        break

for i in range(len(nums)):
    length = 2
    while sum(nums[i:i+length]) < invalid:
        length += 1
    if sum(nums[i:i+length]) == invalid:
        l = nums[i:i+length]
        print(min(l) + max(l))
        break
