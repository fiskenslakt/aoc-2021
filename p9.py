from collections import deque
from functools import reduce
from operator import mul

from aocd import lines

floor = [[int(point) for point in line] for line in lines]

risk_level = 0
low_points = []

for y, row in enumerate(floor):
    for x, point in enumerate(row):
        not_low = False
        for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
            if ((y == 0 and i == -1)
                    or (y == len(floor)-1 and i == 1)
                    or (x == 0 and j == -1)
                    or (x == len(row)-1 and j == 1)):
                continue

            if floor[y][x] >= floor[y+i][x+j]:
                not_low = True
                break

        if not_low:
            continue

        risk_level += floor[y][x] + 1
        low_points.append((x,y))

print('Part 1:', risk_level)

basins = []
for low_point in low_points:
    seen = set()
    queue = deque([low_point])
    basin_size = 0
    while queue:
        x, y = queue.popleft()

        for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
            if ((y == 0 and i == -1)
                    or (y == len(floor)-1 and i == 1)
                    or (x == 0 and j == -1)
                    or (x == len(row)-1 and j == 1)):
                continue

            if (x+j, y+i) not in seen and floor[y+i][x+j] != 9:
                queue.append((x+j, y+i))
                seen.add((x+j, y+i))
                basin_size += 1

    basins.append(basin_size)

print('Part 2:', reduce(mul, sorted(basins, reverse=True)[:3]))
