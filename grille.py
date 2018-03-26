
def rotate_grille(grille):
    return list(zip(*grille[::-1]))

def decrypt(N, grille, text):
    grid = [[None] * N for _ in range(N)]
    text_i = 0
    for _ in range(4):
        for h in range(N):
            for w in range(N):
                if not grille[h][w]:
                    continue
                if grid[h][w] is not None:
                    return 'invalid grille'
                grid[h][w] = text[text_i]
                text_i += 1
        grille = rotate_grille(grille)
    out = ''
    for h in range(N):
        for w in range(N):
            if grid[h][w] is None:
                return 'invalid grille'
            out += grid[h][w]
    return out


def main():
    N = int(input())
    grille = tuple(tuple(c == '.' for c in input()) for _ in range(N))
    cyphertext = input()
    print(decrypt(N, grille, cyphertext))

if __name__ == '__main__':
    main()

