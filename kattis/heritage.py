
BIGPRIME = 1000000007

def count_meanings(d, word, _memo={}):
    if word in _memo:
        return _memo[word]
    meanings = d[word] if word in d else 0
    for i in xrange(1, len(word)):
        f, s = word[:i], word[i:]
        if f in d:
            meanings += d[f] * count_meanings(d, s)
    _memo[word] = meanings % BIGPRIME
    return meanings % BIGPRIME

def main():
    N, name = raw_input().split()
    dictionary = {}
    for _ in xrange(int(N)):
        w, m = raw_input().split()
        dictionary[w] = int(m)

    meanings = count_meanings(dictionary, name)
    print meanings

if __name__ == '__main__':
    main()
