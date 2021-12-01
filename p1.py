from aocd import numbers

increases = 0

for i, j in zip(numbers, numbers[1:]):
    increases += j > i

print('Part 1:', increases)

window_increases = 0

for a, b in zip(zip(numbers,numbers[1:],numbers[2:]), zip(numbers[1:],numbers[2:],numbers[3:])):
    window_increases += sum(a)<sum(b)

print('Part 2:', window_increases)
