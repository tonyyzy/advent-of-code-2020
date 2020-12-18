from functools import reduce


def compute(l):
    brak = 0
    inner = []
    prod = []
    tmp = 0
    op = "+"
    flag = "num"
    for i in l:
        if brak == 0:
            if len(inner) > 0:
                if op == "+":
                    tmp += compute(inner)
                elif op == "*":
                    prod.append(tmp)
                    tmp = compute(inner)
                inner = []
                flag = "op"
            if flag == "num":
                if i[0] != "(":
                    if op == "+":
                        tmp += int(i)
                    elif op == "*":
                        prod.append(tmp)
                        tmp = int(i)
                    flag = "op"
                elif i[0] == "(":
                    brak += i.count("(")
                    inner.append(i[1:])
            elif flag == "op":
                op = i
                flag = "num"
        else:
            if "(" in i:
                brak += i.count("(")
                inner.append(i)
            elif ")" in i:
                brak -= i.count(")")
                if brak == 0:
                    inner.append(i[:-1])
                else:
                    inner.append(i)
            else:
                inner.append(i)
    if len(inner) > 0:
        if op == "+":
            tmp += compute(inner)
        elif op == "*":
            prod.append(tmp)
            tmp = compute(inner)
    prod.append(tmp)
    return reduce(lambda x, y: x * y, prod)


res = 0
with open("day18-1.txt") as f:
    for line in f:
        res += compute(line.strip().split(" "))

print(res)
