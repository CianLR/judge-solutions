import sys

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

for line in sys.stdin.readlines():
    words = line.split()
    tl_words = []
    for word in words:
        first_v = 0
        while word[first_v] not in vowels:
            first_v += 1
        tl_words.append(word[first_v:] + word[:first_v] + ('ay' if first_v else 'yay'))
    print(' '.join(tl_words))
