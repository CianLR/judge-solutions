
def rotate(grid):
    return [list(l[::-1]) for l in zip(*grid)]

def drop(grid):
    for row in range(4):
        new_row = []
        can_merge = False
        for x in grid[row]:
            if x == 0:
                continue
            elif can_merge and new_row[-1] == x:
                new_row[-1] *= 2
                can_merge = False
            else:
                new_row.append(x)
                can_merge = True
        grid[row] = new_row + [0] * (4 - len(new_row))


def main():
    grid = [
        [int(x) for x in raw_input().split()] for _ in range(4)
    ]
    turn = int(raw_input())
    for _ in range((4 - turn) % 4):
        grid = rotate(grid)
    drop(grid)
    for _ in range(turn):
        grid = rotate(grid)
    for l in grid:
        print ' '.join(map(str, l))


if __name__ == '__main__':
    main()

