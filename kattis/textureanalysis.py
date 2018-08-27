
s = input()
i = 1
while s != "END":
    mids = s.split('*')[1:-1]
    if len(set(mids)) <= 1:
        print(i, "EVEN")
    else:
        print(i, "NOT EVEN")
    
    i += 1
    s = input()

