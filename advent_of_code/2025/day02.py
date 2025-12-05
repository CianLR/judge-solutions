import sys


def part1(ranges):
    invalid = 0
    for s, e in ranges:
        for i in range(s, e + 1):
            x = str(i)
            if len(x) % 2 == 0 and x[: len(x) // 2] == x[len(x) // 2 :]:
                invalid += i
    return invalid


def part2(ranges):
    invalid = 0
    for s, e in ranges:
        for i in range(s, e + 1):
            x = str(i)
            for chunk_size in range(1, 1 + (len(x) // 2)):
                if len(x) % chunk_size != 0:
                    continue
                # chunk length is evenly divisible
                for chunk_start in range(0, len(x) - chunk_size, chunk_size):
                    chunk_end = chunk_start + chunk_size
                    if (
                        x[chunk_start:chunk_end]
                        != x[chunk_end : chunk_end + chunk_size]
                    ):
                        break
                else:
                    invalid += i
                    break
    return invalid


def preprocess(lines):
    ret = []
    for pair in lines[0].split(","):
        s, e = pair.split("-")
        ret.append((int(s), int(e)))
    return ret


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
