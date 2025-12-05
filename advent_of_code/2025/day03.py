import sys


def part1(lines):
    jolts = 0
    for line in lines:
        first_i = max(range(len(line) - 1), key=lambda i: line[i])
        second = max(line[first_i + 1 :])
        jolts += (line[first_i] * 10) + second
    return jolts


def part2(lines):
    jolts = 0
    for line in lines:
        j = 0
        last_i = -1
        for digits_left in range(11, -1, -1):
            last_i = max(
                range(last_i + 1, len(line) - digits_left), key=lambda i: line[i]
            )
            j = (j * 10) + line[last_i]
        jolts += j
    return jolts


def preprocess(lines):
    return [[int(x) for x in l.strip()] for l in lines]


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
