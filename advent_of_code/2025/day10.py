import sys
from heapq import heappop, heappush
from itertools import combinations
from functools import reduce

class Machine:
    @staticmethod
    def parse(line):
        indicators, *buttons, joltages = line.split()
        ind = int(indicators[1:-1].replace('.', '0').replace('#', '1')[::-1], 2)
        bs = []
        bi = []
        for b in buttons:
            bs.append(sum(1 << int(i) for i in b[1:-1].split(',')))
            bi.append(tuple(int(i) for i in b[1:-1].split(',')))
        js = [int(j) for j in joltages[1:-1].split(',')]
        return Machine(ind, bs, js, bi)

    def __init__(self, indicators, buttons, joltages, button_indexes):
        self.indicators = indicators
        self.buttons = buttons
        self.button_indexes = button_indexes
        self.joltages = joltages
    
    def check(self, presses):
        res = [0] * len(self.joltages)
        for bi, times in presses:
            for idx in self.button_indexes[bi]:
                res[idx] += times
        if res != self.joltages:
            print(presses)
            print(res, self.joltages)
            return False
        return True


def min_buttons(m):
    for steps in range(1, len(m.buttons)):
        for combo in combinations(m.buttons, steps):
            if reduce(lambda a, b: a ^ b, combo) == m.indicators:
                return steps
    return -1

def joltage_bfs(m):
    queue = [(0, tuple(m.joltages), tuple())]
    visited = set()
    while queue:
        steps, joltages, presses = heappop(queue)
        if joltages in visited:
            continue
        if sum(joltages) == 0:
            m.check(presses)
            return steps
        visited.add(joltages)
        for bi, button in enumerate(m.button_indexes):
            max_presses = min(joltages[idx] for idx in button)
            if max_presses == 0:
                continue
            newj = list(joltages)
            for counter_index in button:
                newj[counter_index] -= max_presses
            heappush(queue, (steps + max_presses, tuple(newj), presses + ((bi, max_presses),)))
    return -1

def part1(macs):
    return sum(min_buttons(m) for m in macs)


def part2(macs):
    return sum(joltage_bfs(m) for m in macs)


def preprocess(lines):
    return [Machine.parse(line) for line in lines]


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <input_file>")
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
    lines = preprocess(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
