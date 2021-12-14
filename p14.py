from collections import Counter, defaultdict

from aocd import submit, data

# data = '''NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C'''

template, rules_raw = data.split('\n\n')

rules = {}
for rule in rules_raw.splitlines():
    a, b = rule.split(' -> ')
    rules[a] = b

polymer = list(template)

for step in range(10):
    insertions = []
    for i in range(len(polymer)-1):
        pair = polymer[i] + polymer[i+1]
        if pair in rules:
            insertions.append((rules[pair], i+1))

    inserts = 0
    for insert, i in insertions:
        polymer.insert(i+inserts, insert)
        inserts += 1

c = Counter(polymer)
print(max(c.items(), key=lambda x: x[1])[1] - min(c.items(), key=lambda x: x[1])[1])

polymer = defaultdict(int)

for i in range(len(template)-1):
    pair = template[i] + template[i+1]
    polymer[pair] += 1

# import pudb;pu.db
for step in range(40):
    new_p = defaultdict(int)
    for pair, amount in polymer.items():
        if pair in rules:
            # polymer[pair] = 0
            a, b = pair
            new_p[a + rules[pair]] += amount
            new_p[rules[pair] + b] += amount

    polymer = new_p

letters = defaultdict(int)
for i, pair in enumerate(polymer):
    letters[pair[0]] += polymer[pair]
    if i == len(polymer) - 1:
        letters[pair[1]] += 1


print(max(letters.items(), key=lambda x: x[1])[1] - min(letters.items(), key=lambda x: x[1])[1])
# print(letters)
print(polymer)
