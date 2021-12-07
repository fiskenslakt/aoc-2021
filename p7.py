from aocd import data, submit

# data = '16,1,2,0,4,2,7,1,2,14'

pos = [int(p) for p in data.split(',')]
best_fuel = float('inf')
best_pos = None
for h in range(min(pos), max(pos)+1):
    fuel = 0
    for p in pos:
        fuel += abs(p - h)

    if fuel < best_fuel:
        best_fuel = fuel
        best_pos = h

print(best_fuel, h)
# submit(best_fuel)

pos = [int(p) for p in data.split(',')]
best_fuel = float('inf')
best_pos = None
for h in range(min(pos), max(pos)+1):
    fuel = 0
    for p in pos:
        fuel += sum(range(1, abs(p - h)+1))

    if fuel < best_fuel:
        best_fuel = fuel
        best_pos = h

# print(best_fuel, best_pos)
submit(best_fuel)
