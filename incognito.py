from collections import defaultdict

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        types = defaultdict(lambda: 1)
        for _ in range(N):
            _, t = input().split()
            types[t] += 1
        disguises = 1
        for t in types:
            disguises *= types[t]
        print(disguises - 1)

if __name__ == '__main__':
    main()

