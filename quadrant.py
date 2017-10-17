
def main():
    x, y = int(input()), int(input())
    print(get_quad(x, y))

def get_quad(x, y):
    if y > 0:
        if x > 0:
            return 1
        else:
            return 2
    else:
        if x < 0:
            return 3
        else:
            return 4


if __name__ == '__main__':
    main()

