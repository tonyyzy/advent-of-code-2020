s = set()
res = []
# with open("day23-test.txt") as f:
#     for line in f:

inp = [int(i) for i in "156794823"] \
    # + list(range(10, 1000001))
hi = max(inp)
lo = 1
# print(inp)
curr_ind = 0
le = len(inp)


def next(inp, curr_ind):
    n3 = [inp[i % le] for i in range(curr_ind + 1, curr_ind + 4)]
    des = inp[curr_ind] - 1
    curr = inp[(curr_ind+4) % le]
    for i in n3:
        inp.remove(i)
    while des < lo or des in n3:
        if des < lo:
            des = hi
        else:
            des -= 1
    ins = inp.index(des)
    inp = inp[: ins + 1] + n3 + inp[ins + 1 :]
    curr_ind = inp.index(curr)
    return inp, curr_ind


for i in range(100):
    inp, curr_ind = next(inp, curr_ind)

i = inp.index(1)
print("".join([str(x) for x in inp[i+1:] + inp[:i]]))


