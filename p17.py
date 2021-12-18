import re

from aocd import submit, data


def triangle_sum(n):
    return (n**2+n)//2


# data = 'target area: x=20..30, y=-10..-5'

x1, x2, y1, y2 = map(int, re.match(r'.+x=(\d+).+?(\d+).+?y=(-?\d+).+?(-?\d+)', data).groups())

# x = 1
# while triangle_sum(x) < x1:
#     x += 1
# min_x = x

# max_y = 0
# y = 0
# while True:
#     y += 1
#     i = 0
#     stop = False
#     while True:
#         i += 1
#         if y2 >= triangle_sum(y) - triangle_sum(i) >= y1:
#             max_y = y
#             break
#         elif triangle_sum(y) - triangle_sum(i) < y1:
#             stop = True
#             break

#     if stop:
#         break



# print(min_x, max_y, triangle_sum(max_y))
# 1653 too low
print('Part 1:', triangle_sum(abs(y1+1)))
