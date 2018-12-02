import sys

def diff(a, b):
    return sum(x != y for x, y in zip(a, b))

def get_cross(a, b):
    return ''.join(x for x, y in zip(a, b) if x == y)

def main():
    boxes = [x.strip() for x in sys.stdin.readlines()]
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            if diff(boxes[i], boxes[j]) == 1:
                print(get_cross(boxes[i], boxes[j]))
                return

if __name__ == '__main__':
    main()

