from aocd import lines

char_map = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
syntax_point_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
auto_point_map = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}
syntax_points = 0
incomplete_lines = []
for line in lines:
    stack = []
    for char in line:
        if char in '([{<':
            stack.append(char)
        elif stack and char_map[char] == stack[-1]:
            stack.pop()
        else:
            syntax_points += syntax_point_map[char]
            break
    else:
        auto_points = 0
        while stack:
            char = stack.pop()
            auto_points *= 5
            auto_points += auto_point_map[char]

        incomplete_lines.append(auto_points)

print('Part 1:', syntax_points)
line_amount = len(incomplete_lines)
print('Part 2:', sorted(incomplete_lines)[line_amount//2])
