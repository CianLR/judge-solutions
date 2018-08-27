import sys

pas, mes = input().split()

mes_i = 0
for i, c in enumerate(pas):
    future = set(pas[i:])
    while mes[mes_i] not in future:
        mes_i += 1
        if mes_i == len(mes):
            print("FAIL")
            sys.exit()

    if mes[mes_i] != c:
        print("FAIL")
        sys.exit()
    mes_i += 1 

print("PASS")
