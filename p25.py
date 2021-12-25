from itertools import count

from aocd import lines

rows = len(lines)
cols = len(lines[0])

_map = {}
east = []
south = []
for y, line in enumerate(lines):
    for x, sc in enumerate(line):
        if sc == '>':
            east.append((x,y))
        elif sc == 'v':
            south.append((x,y))
        _map[(x,y)] = sc

for step in count(1):
    east_move = False
    south_move = False
    new_map = {}
    new_east = []
    for sc in east:
        x, y = sc
        nx = x + 1 if x + 1 < cols else 0
        if _map.get((nx,y), '.') == '.':
            new_map[(nx,y)] = '>'
            new_east.append((nx, y))
            east_move = True
        else:
            new_map[(x,y)] = '>'
            new_east.append((x,y))

    east = new_east
    new_south = []
    for sc in south:
        x, y = sc
        ny = y + 1 if y + 1 < rows else 0
        if new_map.get((x,ny), '.') == '.' and _map.get((x,ny), '.') != 'v':
            new_map[(x,ny)] = 'v'
            new_south.append((x, ny))
            south_move = True
        else:
            new_map[(x,y)] = 'v'
            new_south.append((x,y))

    south = new_south
    _map = new_map
    if not east_move and not south_move:
        break

print('Part 1:', step)
