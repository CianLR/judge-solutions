
def readings_possible(cap, stations):
    on_train = 0
    for left, enter, stay in stations:
        if left > on_train:
            return False
        on_train -= left
        if enter + on_train > cap:
            return False
        on_train += enter
        if on_train < cap and stay > 0:
            return False
    return on_train == 0

def main():
    C, N = map(int, input().split())
    stations = [[int(x) for x in input().split()] for _ in range(N)]
    if readings_possible(C, stations):
        print("possible")
    else:
        print("impossible")


if __name__ == '__main__':
    main()

