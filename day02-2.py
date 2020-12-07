def split_line(line):
    min_max, letter, password = line.split(" ")
    min, max = min_max.split("-")
    letter = letter[0]
    return int(min), int(max), letter, password



entries = []
with open("day02-1.txt") as f:
    for line in f:
        entries.append(split_line(line.strip()))

counter = 0
for entry in entries:
    if (entry[3][entry[0] - 1] == entry[2]) + (entry[3][entry[1] - 1] == entry[2]) == 1:
        counter += 1

print(counter)