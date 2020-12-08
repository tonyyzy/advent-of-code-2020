ops = []
with open("day08-1.txt") as f:
    for line in f:
        ins, arg = line.strip().split(" ")
        arg = int(arg)
        ops.append((ins, arg))

def run(ops):
    accumulator = 0
    counter = [0 for x in range(len(ops))] + [1]
    head = 0
    while counter[head] != 1:
        (ins, arg) = ops[head]
        counter[head] +=1
        if ins == "nop":
            head +=1
        elif ins == "acc":
            accumulator += arg
            head +=1
        elif ins == "jmp":
            head += arg
    if head == len(ops):
        return accumulator
    else:
        return None



for ind, op in enumerate(ops):
    ops_copy = [x for x in ops]
    if op[0] == "jmp":
        ops_copy[ind] = ("nop", op[1])
    elif op[0] == "nop":
        ops_copy[ind] = ("jmp", op[1])
    if x := run(ops_copy):
        print(x)
