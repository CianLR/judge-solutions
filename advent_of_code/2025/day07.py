import sys
from collections import defaultdict


def part1(lines):
    s = lines[0].find('S')
    splits = 0
    beams = {s}
    for line in lines[1:]:
        next_beams = set()
        for b in beams:
            assert 0 <= b < len(line)
            if line[b] == '^':
                splits += 1
                next_beams.add(b - 1)
                next_beams.add(b + 1)
            else:
                next_beams.add(b)
        beams = next_beams
    return splits


def part2(lines):
    s = lines[0].find('S')
    beams = {s: 1}
    for line in lines[1:]:
        next_beams = defaultdict(int)
        for b, v in beams.items():
            assert 0 <= b < len(line)
            if line[b] == '^':
                next_beams[b - 1] += v
                next_beams[b + 1] += v
            else:
                next_beams[b] += v
        beams = next_beams
    return sum(beams.values())


def preprocess(lines):
    return lines


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
