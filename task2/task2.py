import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f1:
    x0, y0 = map(float, f1.readline().split())
    r = float(f1.readline())

with open(file2) as f2:
    points = []
    for line in f2.readlines():
        x, y = map(float, line.split())
        points.append((x, y))

for point in points:
    if (point[0] - x0) ** 2 + (point[1] - y0) ** 2 == r ** 2:
        print(0)
    elif (point[0] - x0) ** 2 + (point[1] - y0) ** 2 < r ** 2:
        print(1)
    else:
        print(2)
