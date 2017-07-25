s = input()
backspaces = s.count('<')
out = [''] * len(s)
ptr = 0
for c in s:
    if c == '<':
        ptr -= 1
        out[ptr] = ''
    else:
        out[ptr] = c
        ptr += 1

print(''.join(out))
