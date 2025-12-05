import sys


def adj(w, h, mw, mh):
    for width in range(w - 1, w + 2):
        for height in range(h - 1, h + 2):
            if width == w and height == h:
                continue
            if 0 <= width < mw and 0 <= height < mh:
                yield width, height


def print_grid(grid):
    for line in grid:
        print("".join(line))
    print()


def part1(lines):
    mh = len(lines)
    mw = len(lines[0])
    acessible = 0
    for h in range(mh):
        for w in range(mw):
            if lines[h][w] == ".":
                continue
            blocked = 0
            for w2, h2 in adj(w, h, mw, mh):
                if lines[h2][w2] == "@":
                    blocked += 1
            if blocked < 4:
                acessible += 1
    return acessible


def part2(lines):
    mh = len(lines)
    mw = len(lines[0])
    removed = 0
    last_removed = -1
    while last_removed != 0:
        last_removed = 0
        for h in range(mh):
            for w in range(mw):
                if lines[h][w] == ".":
                    continue
                blocked = 0
                for w2, h2 in adj(w, h, mw, mh):
                    if lines[h2][w2] == "@":
                        blocked += 1
                if blocked < 4:
                    lines[h][w] = "."
                    removed += 1
                    last_removed = 1
    return removed


def preprocess(lines):
    return [list(line.strip()) for line in lines]


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
