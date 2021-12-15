from heapq import heappush, heappop

from aocd import lines


def dijkstra(graph, target):
    queue = [(0, 0, 0)]  # cur_risk, x, y
    seen = set()
    while queue:
        cr, x, y = heappop(queue)

        if (x, y) == target:
            return cr

        for i, j in ((0,1), (1,0), (-1,0), (0,-1)):
            ix = x+i
            jy = y+j

            if (ix, jy) in graph and (ix, jy) not in seen:
                risk = graph[(ix, jy)]
                heappush(queue, (cr + risk, ix, jy))
                seen.add((ix, jy))


def reset_over_nine(n):
    if n >= 10:
        return n % 10 + 1
    return n


graph = {}
for y in range(len(lines)):
    for x in range(len(lines[0])):
        graph[(x,y)] = int(lines[y][x])

risk = dijkstra(graph, (x, y))
print('Part 1:', risk)

graph = {}
for y in range(len(lines) * 5):
    for x in range(len(lines[0]) * 5):
        risk = int(lines[y % len(lines)][x % len(lines[0])])
        risk = risk + (x // len(lines[0])) + (y // len(lines))
        risk = reset_over_nine(risk)
        graph[(x,y)] = risk

risk = dijkstra(graph, (x, y))
print('Part 2:', risk)
