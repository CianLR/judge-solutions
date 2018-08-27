
def special_divide(N, M):
    shr = len(M) - 1
    if shr == 0:
        return N
    # Check for no decimal
    zero_loc = 0
    for c in N[-shr:][::-1]:
        if c != '0':
            break
        zero_loc += 1
    else:
        return N[:-shr]
    
    # Decimal
    if zero_loc:
        # Chop off trailing
        shr -= zero_loc
        N = N[:-zero_loc]

    assert shr != 0
    if shr < len(N):
        return N[:-shr] + '.' + N[-shr:]
    return '0.' + ('0' * (shr - len(N))) + N


def main():
    N = input()
    M = input()
    print(special_divide(N, M))

if __name__ == '__main__':
    main()

