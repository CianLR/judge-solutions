
class Box:
    def __init__(self, size, x1, y1, x2, y2):
        self.size = size
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def inside(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

def main():
    N = int(input())
    while N:
        boxes = []
        for _ in range(N):
            *coords, size = input().split()
            boxes.append(Box(size, *(float(x) for x in coords)))
        M = int(input())
        for _ in range(M):
            x, y, size = input().split()
            print(size, end=' ')
            x, y = float(x), float(y)
            for b in boxes:
                if b.inside(x, y):
                    print('correct' if b.size == size else b.size)
                    break
            else:
                print("floor")
        print()
        N = int(input())

if __name__ == '__main__':
    main()

