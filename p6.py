from collections import Counter, defaultdict
from aocd import data, submit

# data = '3,4,3,1,2'

fish = [int(f) for f in data.split(',')]
# import pudb;pu.db
for day in range(80):
    old_len = len(fish)
    new_fish = []
    for f in fish:
        if f > 0:
            new_fish.append(f-1)
        else:
            new_fish.append(6)
            new_fish.append(8)

    fish = new_fish

    # print(len(fish), len(fish)-old_len)

print(len(fish))

fish = [int(f) for f in data.split(',')]
fish = Counter(fish)
# import pudb;pu.db
for day in range(256):
    new_fish = defaultdict(int)
    for k, v in fish.items():
        if k > 0:
            new_fish[k-1] += v
        else:
            new_fish[6] += v
            new_fish[8] += v

    fish = new_fish

submit(sum(fish.values()))
