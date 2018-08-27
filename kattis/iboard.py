import sys

for line in sys.stdin.readlines():
    zeros = 0
    ones = 0
    oth_zeros = 0
    oth_ones = 0
    for c in line.strip():
        c_ord = ord(c)
        for p in range(0, 7):
            if c_ord & (1 << p):
                ones += 1
            else:
                zeros += 1

    if ones % 2 or zeros % 2:
        print("trapped")
    else:
        print("free")
