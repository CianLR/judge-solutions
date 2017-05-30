import sys

def is_special(c):
    return 33 <= ord(c) <= 42 or 91 <= ord(c) <= 93

def escape_str(s):
    out = []
    for c in s:
        if is_special(c):
            out.append('\\')
        out.append(c)
    return ''.join(out)

lines = sys.stdin.readlines()
for t in range(0, len(lines), 2):
    s = lines[t + 1].strip()
    for _ in range(int(lines[t])):
        s = escape_str(s)
    print(s)
