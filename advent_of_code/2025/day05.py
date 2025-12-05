import sys
from collections import defaultdict


def part1(lines):
    ranges, ingredients = lines
    fresh = 0
    for ing in ingredients:
        for s, e in ranges:
            if s <= ing <= e:
                fresh += 1
                break
    return fresh


def part2(lines):
    ranges, _ = lines
    ings = 0
    queue = []
    for s, e in ranges:
        queue.append((s, "1s"))
        queue.append((e + 1, "2e"))
    last_start = -1
    open_ranges = 0
    for i, t in sorted(queue):
        if t == "1s":
            if open_ranges == 0:
                last_start = i
            open_ranges += 1
        else:
            open_ranges -= 1
            if open_ranges == 0:
                ings += i - last_start
    return ings


def preprocess(lines):
    ranges = []
    for line in lines:
        if not line.strip():
            break
        s, e = line.strip().split("-")
        ranges.append((int(s), int(e)))
    ingredients = []
    for line in lines[len(ranges) + 1 :]:
        if not line.strip():
            continue
        ingredients.append(int(line.strip()))
    return ranges, ingredients


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <input_file>")
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
    lines = preprocess(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
