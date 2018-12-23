
class Marble:
    def __init__(self, v):
        self.v = v
        self.cw = None
        self.ccw = None

    def insert_cw(self, n):
        n.ccw = self
        n.cw = self.cw
        self.cw.ccw = n
        self.cw = n

    def remove(self):
        self.ccw.cw = self.cw
        self.cw.ccw = self.ccw

def get_highest(players, last_mar):
    scores = [0] * players
    curr = Marble(0)
    curr.cw = curr
    curr.ccw = curr
    for v in xrange(1, last_mar + 1):
        if v % 23 != 0:
            m = Marble(v)
            curr.cw.insert_cw(m)
            curr = m
        else:
            n = curr.ccw.ccw.ccw.ccw.ccw.ccw.ccw
            scores[v % players] += v + n.v
            curr = n.cw
            n.remove()
    return max(scores)

def main():
    PLAYERS = 425
    LAST_MAR = 70848
    print get_highest(PLAYERS, LAST_MAR)

if __name__ == '__main__':
    main()

