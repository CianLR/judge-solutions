from math import log, floor

T = int(input())

for case in range(1, T + 1):
    alnum, sourlang, destlang = input().split()
    sourbase = len(sourlang)
    sour_num = 0
    for c in alnum:
        sour_num = (sour_num * sourbase) + sourlang.index(c)

    destbase = len(destlang)
    dest_num = ''
    power = floor(log(sour_num, destbase))
    for p in range(power, -1, -1):
        power_mul, sour_num = divmod(sour_num, destbase ** p)
        dest_num += destlang[power_mul]
    print("Case #{}:".format(case), dest_num)
