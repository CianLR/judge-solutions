from collections import defaultdict


key_map = {c: (i // 3) + 2 for i, c in enumerate('abcdefghijklmnopqrtuvwxy')}
key_map['s'] = 7
key_map['z'] = 9

def word_to_nums(w):
    return ''.join(str(key_map[c]) for c in w)


if __name__ == '__main__':
    
    word_counts = defaultdict(int)
    N = int(input())
    for _ in range(N):
        word_counts[word_to_nums(input())] += 1

    print(word_counts[input()])
