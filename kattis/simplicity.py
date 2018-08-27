from collections import defaultdict

word = input()
char_freq = defaultdict(int)
for c in word:
    char_freq[c] += 1

to_remove = 0
while len(char_freq) > 2:
    ch = min(char_freq, key=lambda k: char_freq[k])
    to_remove += char_freq[ch]
    del char_freq[ch]

print(to_remove)

