
class Bits:
    def __init__(self):
        self.known = [False] * 32
        self.bits = [None] * 32

    def handle_set(self, i):
        self.known[i] = True
        self.bits[i] = 1

    def handle_clear(self, i):
        self.known[i] = True
        self.bits[i] = 0

    def handle_and(self, i, j):
        if self.known[i] and self.known[j]:
            self.bits[i] &= self.bits[j]
            return
        # Partial known
        if self.known[i]:
            if self.bits[i] == 1:
                self.bits[i] = None
                self.known[i] = False
        elif self.known[j]:
            if self.bits[j] == 0:
                self.known[i] = True
                self.bits[i] = 0

    def handle_or(self, i, j):
        if self.known[i] and self.known[j]:
            self.bits[i] |= self.bits[j]
            return
        # Partial known
        if self.known[i]:
            if self.bits[i] == 0:
                self.bits[i] = None
                self.known[i] = False
        elif self.known[j]:
            if self.bits[j] == 1:
                self.bits[i] = 1
                self.known[i] = True


    def handle_instr(self, ins, *args):
        if ins == 'SET':
            self.handle_set(*args)
        elif ins == 'CLEAR':
            self.handle_clear(*args)
        elif ins == 'AND':
            self.handle_and(*args)
        else:
            self.handle_or(*args)

    def print(self):
        for i in range(31, -1, -1):
            if not self.known[i]:
                print('?', end='')
            else:
                print(self.bits[i], end='')
        print()


def main():
    N = int(input())
    while N != 0:
        bits = Bits()
        for _ in range(N):
            ins, *args = input().split()
            bits.handle_instr(ins, *(int(x) for x in args))
        bits.print()
        N = int(input())

if __name__ == '__main__':
    main()

