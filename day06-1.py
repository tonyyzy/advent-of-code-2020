total = 0
with open("day06-1.txt") as f:
    for group in f.read().split("\n\n"):
        answers = []
        for line in group.split("\n"):
            answers += list(line.strip())
        total += len(set(answers))
    print(total)
