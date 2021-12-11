from collections import deque
from itertools import count, product

from aocd import lines

octopuses = {}

for y, line in enumerate(lines):
    for x, octopus in enumerate(line):
        octopuses[(x,y)] = int(octopus)

flashes = 0

for step in count(1):
    flashed = set()
    flash_ready = deque()
    for octopus in octopuses:
        octopuses[octopus] += 1
        if octopuses[octopus] > 9:
            flash_ready.append(octopus)

    seen = set(flash_ready)
    while flash_ready:
        x, y = flash_ready.popleft()
        flashed.add((x,y))

        octopuses[(x,y)] = 0
        flashes += 1

        for i, j in product((1,0,-1), repeat=2):
            if i == j == 0:
                continue

            ix = x + i
            jy = y + j

            if (ix,jy) in seen:
                continue

            if (ix,jy) in octopuses:
                if octopuses[(ix,jy)] >= 9:
                    flash_ready.append((ix,jy))
                    seen.add((ix,jy))
                else:
                    octopuses[(ix,jy)] += 1

    if step == 100:
        print('Part 1:', flashes)

    if flashed == octopuses.keys():
        break

print('Part 2:', step)
