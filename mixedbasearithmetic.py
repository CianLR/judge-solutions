import sys


for l in sys.stdin.readlines():
    c, i = l.split()
    i = int(i)

    final_num = ''
    carry = 0
    for d in c[::-1]:
        if d.isnumeric():
            i, to_add = divmod(i, 10)
            carry, new_d = divmod(int(d) + to_add + carry, 10)
            final_num = str(new_d) + final_num
        elif d.islower():
            i, to_add = divmod(i, 26)
            carry, new_d = divmod(ord(d) - 97 + to_add + carry, 26)
            final_num = chr(new_d + 97) + final_num
        else:
            i, to_add = divmod(i, 26)
            carry, new_d = divmod(ord(d) - 65 + to_add + carry, 26)
            final_num = chr(new_d + 65) + final_num
    # divmod offsets are -1, I wish I knew why
    i += carry
    while i:
        if final_num[0].isnumeric():
            i, next_d = divmod(i, 10)
            final_num = str(next_d) + final_num
        elif final_num[0].islower():
            i, next_d = divmod(i - 1, 26)
            final_num = chr(next_d + 97) + final_num
        else:
            i, next_d = divmod(i - 1, 26)
            final_num = chr(next_d + 65) + final_num

    print(final_num)

