def id(seat):
    row = list(range(128))
    column = list(range(8))
    for i in seat[:7]:
        if i == "F":
            row = row[:len(row)//2]
        elif i =="B":
            row = row[len(row)//2:]
    for i in seat[7:]:
        if i == "L":
            column = column[:len(column)//2]
        elif i =="R":
            column = column[len(column)//2:]
    return row[0] * 8 +  column[0]

with open("day05-1.txt") as f:
    ids = []
    for line in f:
        ids.append(id(line.strip()))
    print(max(ids))