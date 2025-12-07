import sys

def perform_op(vals, op):
    if op == '*':
        x = 1
        for v in vals:
            x *= v
        return x
    else:
        return sum(vals)


def part1(lines):
    g = [[int(x) if x.isnumeric() else x for x in line.split()] for line in lines]
    lines = list(zip(*g))
    total = 0
    for l in lines:
        total += perform_op(l[:-1], l[-1])
    return total


def part2(lines):
    *lines, ops = lines
    cols = list(zip(*lines))
    vals = [[]]
    for col in cols:
        c = ''.join(col).strip()
        if not c:
            vals.append([])
        else:
            vals[-1].append(int(c))
    total = 0
    for vals, op in zip(vals, ops.split()):
        total += perform_op(vals, op)
    return total


def preprocess(lines):
    return [l for l in lines if l.strip()]


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <input_file>")
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        lines = f.read().split('\n')
    lines = preprocess(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
