from collections import defaultdict
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

#   1:2    4:4
#  ....   ....
# .    c b    c
# .    c b    c
#  ....   dddd
# .    f .    f
# .    f .    f
#  ....   ....

#   7:3     8:7
#  aaaa    aaaa
# .    c  b    c
# .    c  b    c
#  ....    dddd
# .    f  e    f
# .    f  e    f
#  ....    gggg

#   0:6    2:5     3:5
#  aaaa   aaaa    aaaa
# b    c .    c  .    c
# b    c .    c  .    c
#  ....   dddd    dddd
# e    f e    .  .    f
# e    f e    .  .    f
#  gggg   gggg    gggg

#   5:5     6:6    9:6
#  aaaa    aaaa   aaaa
# b    .  b    . b    c
# b    .  b    . b    c
#  dddd    dddd   dddd
# .    f  e    f .    f
# .    f  e    f .    f
#  gggg    gggg   gggg


#
# a - 8 | 6 | 5
# b - 6 | 4 | 3
# c - 8 | 4 | 3
# d - 7 | 5 | 4
# e - 4 | 3 | -
# f - 9 | 5 | 4
# g - 7 | 6 | -

segments = {3:'7', 2:'1', 4:'4', 7:'8'}
freq = 0

for line in lines:
    _input, output = line.split(' | ')
    char_to_digit = {}
    seg_freq = defaultdict(int)
    for digit in _input.split():
        for wire in digit:
            seg_freq[wire] += 1
    freq_seg = {v:k for k, v in seg_freq.items()}
    for digit in output.split():
        if len(digit) in segments:
            freq += 1
            char_to_digit[segments[len(digit)]] = digit

    import pudb;pu.db
    one_seg = set(s['1'])
    four_seg = set(s['4'])
    seven_seg = set(s['7'])
    eight_seg = set(s['8'])

    # eg_seg = eight_seg - four_seg - seven_seg
    bd_seg = four_seg - one_seg
    e_seg = freq_seg[4]
    g_seg = nine_seg - four_seg - seven_seg

    two_seg = None
    three_seg = None
    five_seg = None
    six_seg = None
    nine_seg = eight_seg - e_seg

    a_seg = seven_seg - one_seg
    b_seg = None
    c_seg = None
    d_seg = None
    # e_seg = freq_seg[4]
    f_seg = None
    # g_seg = nine_seg - four_seg - seven_seg

print(freq)
