from math import factorial

def choose(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def catalan(n):
    return choose(n * 2, n) // (n + 1)

def main():
    N = int(input())
    for _ in range(N):
        print(catalan(int(input())))


if __name__ == '__main__':
    main()

