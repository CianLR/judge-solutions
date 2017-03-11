from math import pi

D, V = map(int, input().split())
while D and V:
    large_cyl = pi * (D/2)**2 * D
    
    d_hi = D
    d_lo = 0
    while True:
        d = (d_hi + d_lo) / 2

        small_cyl = pi * (d/2)**2 * d
        two_frustrums = (pi * (D - d) * (D**2 + D * d + d**2)) / 12

        new_V = large_cyl - (small_cyl + two_frustrums)
        
        if abs(new_V - V) < 10**(-8):
            break
        elif new_V > V:
            # Eaten too much, d too small
            d_lo = d
        elif new_V < V:
            # Eaten too little, d too big
            d_hi = d

    print(d)

    D, V = map(int, input().split())
