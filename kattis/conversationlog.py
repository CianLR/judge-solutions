from collections import defaultdict

def main():
    N = int(input())
    word_counts = defaultdict(int)
    words_used = defaultdict(set)
    for _ in range(N):
        name, *words = input().split()
        words_used[name].update(words)
        for w in words:
            word_counts[w] += 1
    
    all_used = min(words_used.values(), key=len).copy()
    for name in words_used:
        all_used &= words_used[name]
        if not all_used:
            print("ALL CLEAR")
            return

    for word in sorted(all_used, key=lambda w: (-word_counts[w], w)):
        print(word)


if __name__ == '__main__':
    main()

