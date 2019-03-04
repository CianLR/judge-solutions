
def main():
    N = int(input())
    qual = 0
    for _ in range(N):
        q, y = [float(x) for x in input().split()]
        qual += q * y
    print(qual)

if __name__ == '__main__':
    main()

