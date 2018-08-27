
class Board:
    def __init__(self):
        # grid[row][col]
        # grid[0][0] is top left
        self.grid = [['']*8 for _ in range(8)]
        for r in range(8):
            for c in range(8):
                self.grid[r][c] = ':::' if (r%2==0) ^ (c%2==0) else '...'

    def add_piece(self, p, is_black):
        if len(p) == 3:
            t, col, row = p
        else:
            t = 'P'
            col, row = p

        if is_black:
            t = t.lower()
        col = 'abcdefgh'.index(col)
        row = 8 - int(row)

        c = self.grid[row][col][0]
        self.grid[row][col] = c + t + c

    def print(self):
        for line in self.grid:
            print('+---+---+---+---+---+---+---+---+')
            print('|' + '|'.join(line) + '|')
        print('+---+---+---+---+---+---+---+---+')

brd = Board()
w = input().split(' ')[1].split(',')
if w == ['']:
    w = []
b = input().split(' ')[1].split(',')
if b == ['']:
    b = []
for p in w:
    brd.add_piece(p, is_black=False)
for p in b:
    brd.add_piece(p, is_black=True)
brd.print()
