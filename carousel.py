
def main():
    N, M = [int(x) for x in input().split()]
    while N != 0 and M != 0:
        tics_price = []
        for _ in range(N):
            a, b = [int(x) for x in input().split()]
            if a <= M:
                tics_price.append((a, b))
        
        if not tics_price:
            print("No suitable tickets offered")
        else:
            tic, price = min(tics_price, key=lambda x: (x[1]/x[0], -x[0]))
            print("Buy {} tickets for ${}".format(tic, price))
        
        N, M = [int(x) for x in input().split()]

if __name__ == '__main__':
    main()

