from collections import defaultdict

def main():
    N = int(input())
    while N != 0:
        words = defaultdict(list)
        for _ in range(N):
            name = input()
            words[name[:2]].append(name)
        for prefix in sorted(words):
            for name in words[prefix]:
                print(name)
        print()
        N = int(input())

if __name__ == '__main__':
    main()

