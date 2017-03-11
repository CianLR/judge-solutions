
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

l = input()
while l != '0':
    rot, txt = l.split()
    rot = int(rot)

    for c in txt[::-1]:
        index = alpha.index(c)
        print(alpha[(index + rot) % len(alpha)], end='')
    print()

    l = input()
