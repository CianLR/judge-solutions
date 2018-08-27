
class Board:
    def __init__(self, R, C):
        self.R = R
        self.C = C
        # self.grid[row][col]
        self.grid = [['#']*C for _ in range(R)]

    def add_char(self, row, col, c):
        self.grid[row][col] = c

    def get_words(self):
        seen = set()
        for r in range(self.R):
            word = ''
            for c in range(self.C):
                char = self.grid[r][c]
                if char == '#':
                    if len(word) >= 2:
                        seen.add(word)
                    word = ''
                else:
                    word += char
            if len(word) >= 2:
                seen.add(word)

        for c in range(self.C):
            word = ''
            for r in range(self.R):
                char = self.grid[r][c]
                if char == '#':
                    if len(word) >= 2:
                        seen.add(word)
                    word = ''
                else:
                    word += char
            if len(word) >= 2:
                seen.add(word)
        return seen
                

R, C = map(int, input().split())
b = Board(R, C)
for r in range(R):
    l = input()
    for c in range(C):
        if l[c] == '#':
            continue
        b.add_char(r, c, l[c])

print(min(b.get_words()))

