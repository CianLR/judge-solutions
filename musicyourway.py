
def main():
    attr_list = input().split()
    attributes = {a: i for i, a in enumerate(attr_list)}
    M = int(input())
    songs = [input().split() for _ in range(M)]
    N = int(input())
    for _ in range(N):
        attr_i = attributes[input()]
        songs = sorted(songs, key=lambda s: s[attr_i])
        print(*attr_list)
        print('\n'.join(' '.join(s) for s in songs))
        print()

if __name__ == '__main__':
    main()

