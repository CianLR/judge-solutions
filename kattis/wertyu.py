import sys

letters = r"1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./".upper()

for line in sys.stdin.readlines():
    line = line.strip('\n')
    for c in line:
        if c == ' ':
            sys.stdout.write(' ')
        else:
            sys.stdout.write(letters[letters.index(c) - 1])
    print()
