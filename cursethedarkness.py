import cmath

def can_read(book, candles, dist=8):
    for c in candles:
        if cmath.polar(book - c)[0] <= dist:
            return True
    return False

def main():
    M = int(input())
    for _ in range(M):
        book = complex(*map(float, input().split()))
        N = int(input())
        candles = [complex(*map(float, input().split())) for _ in range(N)]
        print("light a candle" if can_read(book, candles) else "curse the darkness")

if __name__ == '__main__':
    main()
