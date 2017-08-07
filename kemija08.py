vowels = 'aeiou'

s = input()

i = 0
decoded = ''
while i < len(s):
    decoded += s[i]
    if s[i] in vowels:
        i += 2
    i += 1

print(decoded)
