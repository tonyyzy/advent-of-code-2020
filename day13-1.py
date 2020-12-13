t = []

with open("day13-1.txt") as f:
    time = int(f.readline().strip())
    buses = f.readline().strip()

for bus in buses.split(","):
    if bus != "x":
        t.append((int(bus) - (time % int(bus)), int(bus)))

a, b = sorted(t, key=lambda x: x[0])[0]
print(a * b)

        