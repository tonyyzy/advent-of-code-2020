label = [int(x) for x in "156794823"] + list(range(10, 1000001))
inp = {x: y for x, y in zip(label[:-1], label[1:])}
inp[label[-1]] = label[0]
curr = label[0]

lo = 1
hi = max(label)

def get_des(des, n3):
    des -= 1
    while des < lo or des in n3:
        if des < lo:
            des = hi
        else:
            des -= 1
    return des

for _ in range(10000000):
    n3 = [inp[curr]]
    for i in range(2):
        n3.append(inp[n3[-1]])
    des = get_des(curr, n3)
    n = inp[n3[-1]]
    inp[curr] = n
    n1 = inp[des]
    inp[des] = n3[0]
    inp[n3[-1]] = n1
    curr = n

print(inp[1], inp[inp[1]])