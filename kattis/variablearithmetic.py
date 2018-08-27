
VARS = {}

def assignment(line):
    var, _, i = line.split()
    VARS[var] = int(i)

def expression(line):
    terms = line.split(' + ')
    variables = []
    numeric = 0
    for t in terms:
        if t.isnumeric():
            numeric += int(t)
        elif t in VARS:
            numeric += VARS[t]
        else:
            variables.append(t)

    if numeric:
        print(numeric, "+ " if variables else "", end="")
    print(" + ".join(variables))

def main():
    line = input()
    while line != '0':
        if '=' in line:
            assignment(line)
        else:
            expression(line)
        line = input()

if __name__ == '__main__':
    main()

