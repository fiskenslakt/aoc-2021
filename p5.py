from collections import defaultdict
from aocd import lines, submit


# lines = '''0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2'''.splitlines()

points = defaultdict(int)
# import pudb;pu.db
for line in lines:
    a, b = line.split(' -> ')
    x1, y1 = a.split(',')
    x2, y2 = b.split(',')

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(int(y1), int(y2)+1):
            points[(int(x1),y)] += 1
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(int(x1), int(x2)+1):
            points[(x,int(y1))] += 1
    else:
        if x1 < x2 and y1 < y2:
            for x, y in zip(range(x1,x2+1), range(y1,y2+1)):
                points[(x,y)] += 1
        elif x2 < x1 and y2 < y1:
            for x, y in zip(range(x2,x1+1), range(y2,y1+1)):
                points[(x,y)] += 1
        elif x1 < x2:
            for x, y in zip(range(x1,x2+1), range(y1,y2-1,-1)):
                points[(x,y)] += 1
        elif y1 < y2:
            for x, y in zip(range(x1,x2-1,-1), range(y1,y2+1)):
                points[(x,y)] += 1

submit(sum(p >= 2 for p in points.values()))
