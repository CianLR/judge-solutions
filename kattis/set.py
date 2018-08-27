
def pairwise_or_same(a, b, c):
    return (a != b and b != c and a != c) or (a == b and b == c)

def isset(a, b, c):
    return all(map(lambda x: pairwise_or_same(*x), zip(a, b, c)))

def main():
    cards = []
    for _ in range(4):
        cards.extend(input().split())

    found_set = False
    for i in range(len(cards) - 2):
        for j in range(i + 1, len(cards) - 1):
            for k in range(j + 1, len(cards)):
                if isset(cards[i], cards[j], cards[k]):
                    found_set = True
                    print(i + 1, j + 1, k + 1)
    if not found_set:
        print("no sets")

if __name__ == '__main__':
    main()

