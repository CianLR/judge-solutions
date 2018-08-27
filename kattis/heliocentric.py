import sys

E_DAYS = 365
M_DAYS = 687

for tc, line in enumerate(sys.stdin.readlines()):
    e, m = map(int, line.split())
    if e == 0 and m == 0:
        print("Case {}:".format(tc+1), 0)
        continue
    elif E_DAYS - e > M_DAYS - m:
        m += (E_DAYS - e)
        m %= M_DAYS
        days_added = (E_DAYS - e)
        e = 0
    elif M_DAYS - m > E_DAYS - e:
        e += (M_DAYS - m)
        e %= E_DAYS
        days_added = (M_DAYS - m)
        m = 0
    else:
        print("Case {}:".format(tc+1), M_DAYS - m)
        continue

    while e or m:
        if e:
            m = (m + (E_DAYS - e)) % M_DAYS
            days_added += (E_DAYS - e)
            e = 0
        else:
            e = (e + (M_DAYS - m)) % E_DAYS
            days_added += (M_DAYS - m)
            m = 0
    print("Case {}:".format(tc+1), days_added)
