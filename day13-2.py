from functools import reduce

def egcd(a, b):
    b0 = b
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
        print(q, a, b, x0, x1)
    if x1 < 0: x1 += b0
    return x1

with open("day13-1.txt") as f:
    time = int(f.readline().strip())
    buses = f.readline().strip()

t = []
b = []
for ind, bus in enumerate(buses.split(",")):
    if bus != "x":
        t.append(-ind)
        b.append(int(bus))


# tot = reduce(lambda x, y: x * y, b)
# res = 0
# for i, j in zip(t, b):
#     rest = tot // j
#     s = egcd(rest, j)
#     res += s * rest * i
#     print(i, s, rest)
# print(res % tot)
print(egcd(19, 17))
