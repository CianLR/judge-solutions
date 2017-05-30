import sys

def check_golomb(marks):
    possibles = set()
    for i in range(len(marks)):
        for j in range(i + 1, len(marks)):
            rule = abs(marks[i] - marks[j])
            if rule in possibles:
                return 'not a ruler'
            possibles.add(rule)
    missing = []
    for i in range(1, max(marks) + 1):
        if i not in possibles:
            missing.append(str(i))
    return ('missing ' + ' '.join(missing)) if missing else 'perfect'

for line in sys.stdin.readlines():
    marks = [int(x) for x in line.split()]
    print(check_golomb(marks))
