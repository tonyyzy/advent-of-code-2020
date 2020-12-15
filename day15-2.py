s = [2,20,0,4,1,17]
num = {x: ind + 1 for ind, x in enumerate(s)}
last = 0
for i in range(len(s), 30000000):
    c = last
    if c not in num.keys():
        last = 0
    else:
        last = i + 1 - num[c]
    num[c] = i +1
# print(num)
print(c)

