

def rot90(grid):
    return [''.join(s)[::-1] for s in zip(*grid)]

def rot45(grid, H, W):
    SZ = H + W - 1
    rgrid = [[' ']*SZ for _ in range(SZ)]
    w_offset = H - 1
    h_offset = 0
    for row in grid:
        for i, c in enumerate(row):
            rgrid[h_offset + i][w_offset + i] = c
        w_offset -= 1
        h_offset += 1
    return [''.join(line) for line in rgrid]

def main():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(input())
    A = int(input())
    for _ in range((A % 360) // 90):
        grid = rot90(grid)
        H, W = W, H
    if A % 90 == 45:
        grid = rot45(grid, H, W)
    
    for line in grid:
        print(line)


if __name__ == '__main__':
    main()

