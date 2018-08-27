

def match(pattern, name):
    sub_matches = pattern.split('*')
    if len(sub_matches) < 2:
        return name == pattern or pattern == '*'
    start, *matches, end = sub_matches
    if not name.startswith(start):
        return False
    name = name[len(start):]
    if not name.endswith(end):
        return False
    name = name[:len(name)-len(end)]
    # Assuming *...*
    matches = [m for m in matches if m]
    i = -1
    for m in matches:
        i = name.find(m, i + 1)
        if i == -1:
            return False
    return True

def main():
    P = input()
    N = int(input())
    for _ in range(N):
        f = input()
        if match(P, f):
            print(f)

if __name__ == '__main__':
    main()

