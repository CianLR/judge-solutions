import sys

seen = set()
for line in sys.stdin.readlines():
    out_line = []
    for w in line.split():
        if w.lower() in seen:
            out_line.append('.')
        else:
            out_line.append(w)
            seen.add(w.lower())
    print(' '.join(out_line))
