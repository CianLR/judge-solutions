

def main():
    quants = [int(x) for x in input().split()]
    ratios = [int(x) for x in input().split()]

    for q, r in zip(quants, ratios):
        lit_per_unit = q / r
        remainders = []
        for qu, ra in zip(quants, ratios):
            remainders.append(round(qu - (ra * lit_per_unit), 4))
            if remainders[-1] < 0:
                break
        else:
            print(*remainders)
            break

if __name__ == '__main__':
    main()

