
def digit_sum(n):
    tot = 0
    while n > 0:
        tot += n%10
        n //= 10
    return tot

n = int(input())
while n != 0:
    n_sum = digit_sum(n)
    i = 11
    while True:
        if digit_sum(n*i) == n_sum:
            print(i)
            break
        i += 1

    n = int(input())