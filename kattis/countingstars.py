from sys import stdin
from collections import deque

def fill(R, C, sky, r, c):
    q = deque([(r, c)])
    sky[r][c] = False
    while q:
        r, c = q.pop()
        for rm, cm in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + rm
            nc = c + cm
            if 0 <= nr < R and 0 <= nc < C and sky[nr][nc]:
                sky[nr][nc] = False
                q.append((nr, nc))

def count_stars(R, C, sky):
    stars = 0
    for r in range(R):
        for c in range(C):
            if sky[r][c]:
                fill(R, C, sky, r, c)
                stars += 1
    return stars

def main():
    rc = stdin.readline().strip()
    case = 0
    while rc:
        case += 1
        R, C = map(int, rc.split())
        sky = [
            [c == '-' for c in stdin.readline().strip()] for _ in range(R)
        ]
        print("Case {}:".format(case), count_stars(R, C, sky))
        rc = stdin.readline().strip()

if __name__ == '__main__':
    main()

