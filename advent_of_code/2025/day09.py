import sys


def part1(lines):
    max_area = 0
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            ix, iy = lines[i]
            jx, jy = lines[j]
            area = (abs(jx - ix) + 1) * (abs(jy - iy) + 1)
            max_area = max(max_area, area)
    return max_area


def part2(lines):
    return 0


def preprocess(lines):
    return [tuple(map(int, line.split(","))) for line in lines]


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
