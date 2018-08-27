s = ['all my indicies were off by 1 and I am not going to redo them',
    '+---+',
    '|   |',
    '+   +',
    '    +',
    '    |',
    '|    ',
    '+    ']

nums = {
    '0': [s[i] for i in [1, 2, 2, 3, 2, 2, 1]],
    '1': [s[i] for i in [4, 5, 5, 4, 5, 5, 4]],
    '2': [s[i] for i in [1, 5, 5, 1, 6, 6, 1]],
    '3': [s[i] for i in [1, 5, 5, 1, 5, 5, 1]],
    '4': [s[i] for i in [3, 2, 2, 1, 5, 5, 4]],
    '5': [s[i] for i in [1, 6, 6, 1, 5, 5, 1]],
    '6': [s[i] for i in [1, 6, 6, 1, 2, 2, 1]],
    '7': [s[i] for i in [1, 5, 5, 4, 5, 5, 4]],
    '8': [s[i] for i in [1, 2, 2, 1, 2, 2, 1]],
    '9': [s[i] for i in [1, 2, 2, 1, 5, 5, 1]],
    ':': [' ', ' ', 'o', ' ', 'o', ' ', ' ']
}


# for l in nums['0']:
#     print(l)

time = input()
while time != 'end':
    lines = [''] * 7
    for c in time:
        for i, l in enumerate(nums[c]):
            lines[i] += l + '  '

    for l in lines:
        print(l[:-2])
    print()
    print()
    time = input()
print('end')
