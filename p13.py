from aocd import data

dots_raw, folds = data.split('\n\n')

dots = set()
for dot in dots_raw.splitlines():
    x, y  = dot.split(',')
    dots.add((int(x), int(y)))

for i, fold in enumerate(folds.splitlines()):
    fold = fold.split()[-1]
    axis, n = fold.split('=')

    for x, y in dots.copy():
        if axis == 'y' and y > int(n):
            dots.discard((x,y))
            dots.add((x, int(n)*2-y))
        elif axis == 'x' and x > int(n):
            dots.discard((x,y))
            dots.add((int(n)*2-x, y))

    if i == 0:
        print('Part 1:', len(dots))

print('Part 2:')
for y in range(max(dots, key=lambda d: d[1])[1]+1):
    for x in range(max(dots, key=lambda d: d[0])[0]+1):
        if (x, y) in dots:
            print('\u2588', end='')
        else:
            print(' ', end='')
    print()
