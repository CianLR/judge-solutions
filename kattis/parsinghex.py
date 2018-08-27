import sys

def print_hex(hl):
    hx = '0x' + ''.join(hl)
    i = int(hx, 16)
    print(hx, i)

hex_chars = {
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    'a', 'b', 'c', 'd', 'e', 'f',
    'A', 'B', 'C', 'D', 'E', 'F'
}
for line in sys.stdin.readlines():
    curr_hex = []
    hex_hunt = False
    skip = False
    for i in range(1, len(line)):
        if skip:
            skip = False
            continue
        if hex_hunt:
            if line[i] in hex_chars:
                curr_hex.append(line[i])
            else:
                print_hex(curr_hex)
                curr_hex = []
                hex_hunt = False
                skip = True
        else:
            if line[i].lower() == 'x' and line[i - 1] == '0':
                hex_hunt = True
