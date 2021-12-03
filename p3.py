from aocd import lines, submit


# lines = '''00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010'''.splitlines()

e = []
g = []

bits = zip(*lines)
# import pudb;pu.db
for bit in bits:
    if bit.count('1') > bit.count('0'):
        g.append('1')
        e.append('0')
    else:
        g.append('0')
        e.append('1')

gamma = int(''.join(g), 2)
ep = int(''.join(e), 2)

# print(gamma, ep)
# submit(gamma*ep)
diag = lines.copy()
# for i, bit in enumerate(zip(*diag)):
i = 0
# import pudb;pu.db
while True:
    bit = list(zip(*diag))[i]
    keep = []
    if bit.count('1') > bit.count('0') or bit.count('1') == bit.count('0'):
        for line in diag:
            if line[i] == '1':
                keep.append(line)
    elif bit.count('0') > bit.count('1'):
        for line in diag:
            if line[i] == '0':
                keep.append(line)

    diag = keep
    i += 1
    if len(keep) == 1:
        break
oxygen = int(keep[0],2)

i = 0
# import pudb;pu.db
diag = lines.copy()
while True:
    bit = list(zip(*diag))[i]
    keep = []
    if bit.count('1') < bit.count('0'):
        for line in diag:
            if line[i] == '1':
                keep.append(line)
    elif bit.count('0') < bit.count('1') or bit.count('1') == bit.count('0'):
        for line in diag:
            if line[i] == '0':
                keep.append(line)

    diag = keep
    i += 1
    if len(keep) == 1:
        break
co2 = int(keep[0],2)

submit(oxygen*co2)
