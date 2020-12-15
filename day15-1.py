num = {}
s = [2,20,0,4,1,17]
for i in range(2020):
    if i < len(s):
        c = s[i]
    else:
        c = last
    if c not in num.keys():
        last = 0
    else:
        last = i + 1 - num[c]
    num[c] = i +1
# print(num)
print(c)



