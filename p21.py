from collections import deque

from aocd import lines


class Die:
    value = 0
    rolls = 0

    def __next__(self):
        self.value += 1
        self.rolls += 1
        if self.value == 101:
            self.value = 1
        return self.value


# lines = '''Player 1 starting position: 4
# Player 2 starting position: 8'''.splitlines()

p1, p2 = lines
p1_pos = int(p1[-1])
p2_pos = int(p2[-1])

die = Die()
p1_pawn = deque(list(range(p1_pos,11)) + list(range(1, p1_pos)))
p2_pawn = deque(list(range(p2_pos,11)) + list(range(1, p2_pos)))
p1_score = 0
p2_score = 0

while True:
    spaces = 0
    for _ in range(3):
        spaces += next(die)

    p1_pawn.rotate(-(spaces % 10))
    p1_score += p1_pawn[0]

    if p1_score >= 1000:
        ans = p2_score * die.rolls
        break

    spaces = 0
    for _ in range(3):
        spaces += next(die)

    p2_pawn.rotate(-(spaces % 10))
    p2_score += p2_pawn[0]

    if p2_score >= 1000:
        ans = p1_score * die.rolls
        break

print('Part 1:', ans)
