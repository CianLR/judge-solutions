
def check_valid(queens):
    return (len(set(q[0] for q in queens)) == 8 and
            len(set(q[1] for q in queens)) == 8 and
            len(set(q[0] - q[1] for q in queens)) == 8 and
            len(set(-q[0] - q[1] for q in queens)) == 8)


def main():
    queens = []
    for i in range(8):
        for j, c in enumerate(input()):
            if c == '*':
                queens.append((i, j))
    print("valid" if check_valid(queens) else "invalid")

# This is pointless because you can't import this file anyhow
if __name__ == '__main__':
    main()

