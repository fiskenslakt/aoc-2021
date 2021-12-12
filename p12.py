from collections import defaultdict

from aocd import lines


class CaveSystem:
    graph = defaultdict(list)
    paths = 0

    def __init__(self, caves):
        for cave in caves:
            a, b = cave.split('-')
            self.graph[a].append(b)
            self.graph[b].append(a)

    def part_one(self, src, seen):
        seen = seen.copy()
        if src == 'end':
            self.paths += 1
            return

        if src.islower():
            seen.add(src)

        for child in self.graph[src]:
            if child not in seen:
                self.part_one(child, seen)

    def part_two(self, src, seen):
        seen = seen.copy()
        if src == 'end':
            self.paths += 1
            return

        if src.islower():
            seen[src] += 1

        for child in self.graph[src]:
            if child != 'start' and (2 not in seen.values() or child not in seen):
                self.part_two(child, seen)


cs = CaveSystem(lines)
cs.part_one('start', set())
print('Part 1:', cs.paths)

cs.paths = 0  # reset path count
cs.part_two('start', defaultdict(int))
print('Part 2:', cs.paths)
