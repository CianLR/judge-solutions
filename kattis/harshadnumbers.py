
def is_harshad(n):
    return n % sum(int(x) for x in str(n)) == 0

def main():
    N = int(input())
    for n in range(N, 1000000001):
        if is_harshad(n):
            print(n)
            break

if __name__ == '__main__':
    main()

