from collections import defaultdict

s = input()
char_freq = defaultdict(int)
for c in s:
    char_freq[c] += 1

odds = 0
for v in char_freq.values():
    if v % 2:
        odds += 1

print(max(0, odds - 1))
