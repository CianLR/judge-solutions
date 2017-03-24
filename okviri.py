word = input()

line_2 = '.'
for i in range(len(word)):
    if i % 3 == 2:
        line_2 += '.*..'
    else:
        line_2 += '.#..'

line_1 = '.'
for i in range(len(word)):
    if i % 3 == 2:
        line_1 += '*.*.'
    else:
        line_1 += '#.#.'

line_0 = '#'
for i, c in enumerate(word):
    if i % 3 == 1 and len(word) - 1 != i:
        line_0 += '.{}.*'.format(c)
    elif i % 3 == 2:
        line_0 += '.{}.*'.format(c)
    else:
        line_0 += '.{}.#'.format(c)

print(line_2)
print(line_1)
print(line_0)
print(line_1)
print(line_2)
