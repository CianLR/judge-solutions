
class Piece:
    def __init__(self, t, r, c):
        self.is_white = t.isupper()
        self.p_type = t.upper()
        self.row = r
        self.col = c

    def nice_repr(self):
        tpe = self.p_type if self.p_type != 'P' else ''
        return tpe + 'abcdefgh'[self.col] + str(self.row + 1)

    def __eq__(self, other):
        return self.p_type == other.p_type and self.row == other.row and self.col == other.col

    def __gt__(self, other):
        order = 'PNBRQK'
        if order.index(self.p_type) != order.index(other.p_type):
            return order.index(self.p_type) < order.index(other.p_type)
        elif self.row != other.row:
            if self.is_white:
                return self.row > other.row
            else:
                return self.row < other.row
        elif self.col != other.col:
            return self.col > other.col
        return False

    def __lt__(self, other):
        return (not self > other) and (not self == other)

whites = []
blacks = []

for r in range(7, -1, -1):
    input()
    sqs = input()[2::4]
    for c, p_char in enumerate(sqs):
        if p_char == ':' or p_char == '.':
            continue
        p = Piece(p_char, r, c)
        if p.is_white:
            whites.append(p)
        else:
            blacks.append(p)

# King should be smallest, lowest row smaller (if white), lowest col smaller
print('White:', ','.join([p.nice_repr() for p in sorted(whites)]))
print('Black:', ','.join([p.nice_repr() for p in sorted(blacks)]))
