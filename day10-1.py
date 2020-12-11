jolts = []

with open("day10-1.txt") as f:
    for line in f:
        jolts.append(int(line.strip()))

diff = []
jolts = sorted(jolts)
diff.append(jolts[0] - 0)
for i in range(1, len(jolts)):
    diff.append(jolts[i] - jolts[i - 1])
# print(jolts)
# print(diff.count(1), (diff.count(3) + 1))
print(diff.count(1) * (diff.count(3) + 1))