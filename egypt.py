
def get():
    return sorted(int(x) for x in input().split())

def main():
    a, b, c = get()
    while a or b or c:
        if a ** 2 + b ** 2 == c ** 2:
            print("right")
        else:
            print("wrong")
        a, b, c = get()


if __name__ == '__main__':
    main()

