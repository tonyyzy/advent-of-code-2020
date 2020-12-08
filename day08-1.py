accumulator = 0
ops = []
with open("day08-1.txt") as f:
    for line in f:
        ins, arg = line.strip().split(" ")
        arg = int(arg)
        ops.append((ins, arg))
counter = [0 for x in range(len(ops))]
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

print(accumulator)
