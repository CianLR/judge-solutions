from collections import deque

def adj(N, grid, x, y, seen, col):
    for xm, ym in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        xn, yn = x + xm, y + ym
        if 0 <= xn < N and 0 <= yn < N and grid[xn][yn] == col and (xn, yn) not in seen:
            yield xn, yn

def bfs(N, grid, starts, col):
    q = deque(starts)
    seen = set(starts)
    while q:
        x, y = q.popleft()
        for xn, yn in adj(N, grid, x, y, seen, col):
            seen.add((xn, yn))
            q.append((xn, yn))
    return seen

def set_colour(N, grid, to_set, col):
    for x, y in to_set:
        grid[x][y] = col

def greedy_fill(N, grid):
    filled = bfs(N, grid, [(0, 0)], grid[0][0])
    colour_choices = [0] * 6
    while len(filled) < (N * N):
        best_col = None
        best_set = set()
        for c in xrange(6):
            new_filled = bfs(N, grid, filled, c)
            if len(new_filled) > len(best_set):
                best_set = new_filled
                best_col = c
        set_colour(N, grid, best_set, best_col)
        filled = best_set
        colour_choices[best_col] += 1
    return sum(colour_choices), colour_choices

def main():
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        grid = [[int(x) - 1 for x in raw_input()] for _ in xrange(N)]
        moves, colours = greedy_fill(N, grid)
        print moves
        print ' '.join(map(str, colours))

if __name__ == '__main__':
    main()

