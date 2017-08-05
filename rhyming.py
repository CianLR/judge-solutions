
class RhymeChecker:
    def __init__(self):
        self.rhyme_sets = []

    def add_set(self, l):
        self.rhyme_sets.append(l)

    def has_prefix(self, l, w):
        for test in l:
            if w.endswith(test):
                return True
        return False

    def check_rhyme(self, a, b):
        for rh in self.rhyme_sets:
            if self.has_prefix(rh, a) and self.has_prefix(rh, b):
                return True
        return False

def main():
    word = input()
    R = int(input())
    r = RhymeChecker()
    for _ in range(R):
        r.add_set(input().split())
    W = int(input())
    for _ in range(W):
        if r.check_rhyme(word, input()):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()

