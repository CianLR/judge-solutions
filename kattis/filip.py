A, B = input().split()

Af, Bf = int(A[::-1]), int(B[::-1])
if Af > Bf:
    print(Af)
else:
    print(Bf)
