grid = []
with open("day03-1.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

pos = [0, 0]
grid_len = len(grid)
grid_wid = len(grid[0])
counter = 0
while pos[1] < grid_len:
    pos[0] += 3
    pos[1] += 1
    pos[0] %= grid_wid
    if pos[1] < grid_len and grid[pos[1]][pos[0]] == "#":
        counter += 1
print(counter)