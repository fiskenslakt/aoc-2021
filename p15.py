from heapq import heappush, heappop

from aocd import submit, lines

# lines = '''1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581'''.splitlines()

graph = {}
for y in range(len(lines)):
    for x in range(len(lines[0])):
        graph[(x,y)] = int(lines[y][x])

target = (x, y)

queue = [(0,1,0,0)]  # cur_risk, next_risk, x, y
seen = set()
while queue:
    cr, r, x, y = heappop(queue)

    if (x, y) == target:
        print(cr)
        break

    for i, j in ((0,1), (1,0), (-1,0), (0,-1)):
        ix = x+i
        jy = y+j

        if (ix,jy) in graph and (ix,jy) not in seen:
            risk = graph[(ix,jy)]
            heappush(queue, (cr+risk, risk, ix, jy))
            seen.add((ix,jy))
