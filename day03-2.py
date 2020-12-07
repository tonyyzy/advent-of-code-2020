def trees(grid, x, y):
    pos = [x, y]
    grid_len = len(grid)
    grid_wid = len(grid[0])
    counter = 0
    while pos[1] < grid_len:
        if grid[pos[1]][pos[0]] == "#":
            counter += 1
        pos[0] += x
        pos[1] += y
        pos[0] %= grid_wid
    return counter


grid = []
with open("day03-1.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

print(len(grid), len(grid[0]))

prod = 1
for (x, y) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    prod *= trees(grid, x, y)
    print(trees(grid, x, y))
print(prod)