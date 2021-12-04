import re
from collections import defaultdict
from aocd import data, submit

# data = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7'''


draws, boards_raw = data.split('\n\n', 1)
# import pudb;pu.db
boards_raw = boards_raw.split('\n\n')
boards = []
for i in range(len(boards_raw)):
    boards.append([])
    for j, row in enumerate(boards_raw[i].splitlines()):
        boards[i].append([])
        for n in re.findall(r'\d+', row):
            boards[i][j].append(int(n))


bingo = [defaultdict(bool) for _ in range(len(boards))]
winners = []
for draw in map(int, draws.split(',')):
    for b, board in enumerate(boards):
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == draw:
                    bingo[b][(i, j)] = True
    # check boards for bingo
    for b in range(len(boards)):
        for row in range(5):
            if all(bingo[b][(row, col)] for col in range(5)):
                # marked = [(row,col) for col in range(5)]
                unmarked = []
                for i in range(5):
                    for j in range(5):
                        # import pudb;pu.db
                        if not bingo[b][(i,j)]:
                            unmarked.append(boards[b][i][j])

                # print(sum(unmarked), draw, sum(unmarked)*draw)
                # submit(sum(unmarked)*draw)
                # raise SystemExit
                if b not in winners:
                    winners.append(b)
                    if len(winners) == len(boards):
                        print(sum(unmarked), draw, sum(unmarked)*draw)
                        submit(sum(unmarked)*draw)
                        raise SystemExit
        for col in range(5):
            if all(bingo[b][(row, col)] for row in range(5)):
                unmarked = []
                for i in range(5):
                    for j in range(5):
                        # import pudb;pu.db
                        if not bingo[b][(i,j)]:
                            unmarked.append(boards[b][i][j])

                # print(sum(unmarked), draw, sum(unmarked)*draw)
                # submit(sum(unmarked)*draw)
                # raise SystemExit
                if b not in winners:
                    winners.append(b)
                    if len(winners) == len(boards):
                        print(sum(unmarked), draw, sum(unmarked)*draw)
                        submit(sum(unmarked)*draw)
                        raise SystemExit
