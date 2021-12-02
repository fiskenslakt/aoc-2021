from aocd import lines

horizontal = 0
depth = 0
aim = 0

for line in lines:
    direction, amount = line.split()
    if direction == 'forward':
        horizontal += int(amount)
        depth += int(amount) * aim
    elif direction == 'down':
        aim += int(amount)
    elif direction == 'up':
        aim -= int(amount)

print('Part 1:', horizontal * aim)
print('Part 2:', horizontal * depth)
