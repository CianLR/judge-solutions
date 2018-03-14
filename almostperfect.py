import sys
from math import floor

def get_divisors(n):
    div = {1}
    for i in range(2, 1 + int(floor(n ** 0.5))):
        if n % i == 0:
            div.add(i)
            div.add(n // i)
    return div

def main():
    for line in sys.stdin.readlines():
        n = int(line.strip())
        div_sum = sum(get_divisors(n))
        if n == div_sum:
            print(n, "perfect")
        elif abs(n - div_sum) <= 2:
            print(n, "almost perfect")
        else:
            print(n, "not perfect")

if __name__ == '__main__':
    main()

