from functools import reduce

from aocd import lines, submit

#    0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

easy_digits = 0
output_total = 0

for line in lines:
    signals, digits = line.split(' | ')

    five_segs = []
    six_segs = []
    for signal in signals.split():
        if len(signal) == 2:
            cf = set(signal)
        elif len(signal) == 3:
            acf = set(signal)
        elif len(signal) == 4:
            bcdf = set(signal)
        elif len(signal) == 5:
            five_segs.append(set(signal))
        elif len(signal) == 6:
            six_segs.append(set(signal))
        elif len(signal) == 7:
            abcdefg = set(signal)

    a = acf - cf
    bd = bcdf - cf
    eg = abcdefg - bcdf - a
    adg = reduce(set.intersection, five_segs)  # 2, 3, 5
    b = bd - adg
    abcefg = eg | acf | b
    abfg = reduce(set.intersection, six_segs)  # 0, 6, 9
    d = abcdefg - abcefg
    g = adg - a - d
    f = abfg - a - b - g
    abdfg = a | b | d | f | g
    ce = abcefg - abdfg
    c = cf - f
    e = ce - c

    zero = frozenset(a | b | c | e | f | g)
    one = frozenset(c | f)
    two = frozenset(a | c | d | e | g)
    three = frozenset(a | c | d | f | g)
    four = frozenset(b | c | d | f)
    five = frozenset(a | b | d | f | g)
    six = frozenset(a | b | d | e | f | g)
    seven = frozenset(a | c | f)
    eight = frozenset(a | b | c | d | e | f | g)
    nine = frozenset(a | b | c | d | f | g)

    seg_to_num = {
        zero: '0',
        one: '1',
        two: '2',
        three: '3',
        four: '4',
        five: '5',
        six: '6',
        seven: '7',
        eight: '8',
        nine: '9'
    }

    output = ''
    for digit in digits.split():
        if len(digit) in {2, 3, 4, 7}:
            easy_digits += 1

        output += seg_to_num[frozenset(digit)]

    output_total += int(output)

print('Part 1:', easy_digits)
print('Part 2:', output_total)
