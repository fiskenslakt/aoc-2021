import re

from aocd import  data


def triangle_sum(n):
    return (n**2+n)//2


x1, x2, y1, y2 = map(int, re.match(r'.+x=(\d+).+?(\d+).+?y=(-?\d+).+?(-?\d+)', data).groups())

max_y = abs(y1+1)
print('Part 1:', triangle_sum(max_y))

velocity_values = set()

for x in range(1, x2+1):
    for y in range(y1, max_y+1):
        vx = px = x
        vy = py = y
        while True:
            if px > x2 or py < y1:
                break
            if x1 <= px <= x2 and y1 <= py <= y2:
                velocity_values.add((x, y))

            vx -= 1 if vx > 0 else 0
            vy -= 1

            px += vx
            py += vy

print('Part 2:', len(velocity_values))
