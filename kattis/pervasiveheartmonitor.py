import sys

for line in sys.stdin.readlines():
    line_lst = line.strip().split()
    name = []
    rates = []
    for chunk in line_lst:
        if chunk.isalpha():
            name.append(chunk)
        else:
            rates.append(float(chunk))
    print(sum(rates)/len(rates), ' '.join(name))
