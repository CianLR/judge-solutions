import sys


def part1(lines):
    dial = 50
    count = 0
    for d, c in lines:
        if d == "L":
            dial = (dial - c) % 100
        else:
            dial = (dial + c) % 100
        if dial == 0:
            count += 1
    return count


def part2(lines):
    dial = 50
    count = 0
    for d, c in lines:
        if d == "L":
            for _ in range(c):
                dial -= 1
                if dial == 0:
                    count += 1
                elif dial < 0:
                    dial = 99
        else:
            for _ in range(c):
                dial += 1
                if dial == 100:
                    count += 1
                    dial = 0
    return count


def preprocess(lines):
    return [(l[0], int(l[1:])) for l in lines]


def main():
    import sys

    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
    lines = preprocess(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
