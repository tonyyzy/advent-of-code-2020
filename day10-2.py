jolts = [0]

with open("day10-1.txt") as f:
    for line in f:
        jolts.append(int(line.strip()))

jolts.append(max(jolts) + 3)
jolts = sorted(jolts)

def diff(j):
    d = []
    for i in range(1, len(j) -1):
        if (j[i+1] - j[i-1]) < 4:
            d.append(i)
    return d
    
checked = set()

head = 0
tail = 0
d = diff(jolts)
tot = 1
for i in range(1, len(d)):
    if d[i] - d[i - 1] == 1:
        tail = i
    else:
        l = tail - head + 1
        low = jolts[d[head] - 1]
        high = jolts[d[tail] + 1]
        coeff = 0
        if l == 1:
            coeff = 2
        elif l == 2:
            coeff = 4
        elif l == 3 and high - low == 3:
            coeff = 8
        else:
            coeff = 7
        tot *= coeff
        # print(l, head, tail, low, high, coeff)
        head = tail + 1
        tail += 1
l = tail - head + 1
low = jolts[d[head] - 1]
high = jolts[d[tail] + 1]
coeff = 0
if l == 1:
    coeff = 2
elif l == 2:
    coeff = 4
elif l == 3 and high - low == 3:
    coeff = 8
else:
    coeff = 7
tot *= coeff
# print(l, head, tail, low, high, coeff)
head = tail + 1
tail += 1
print(tot)



# print(list(enumerate(jolts)))
# print(list(enumerate(diff(jolts))))
# print(arr(jolts, []))
# print(checked)
# print(len(checked) + 1)
