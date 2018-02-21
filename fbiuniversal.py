
CONFUSING_TRANS = str.maketrans("BGIOQSUYZ", "8C1005VV2")

def translate(s):
    return s.translate(CONFUSING_TRANS)

def char_val(c):
    return "0123456789ACDEFHJKLMNPRTVWX".index(c)

def dec_to_char(d):
    return "0123456789ACDEFHJKLMNPRTVWX"[d]

def check_digit(s):
    coeff = (2, 4, 5, 7, 8, 10, 11, 13)
    check = 0
    for i in range(8):
        check += coeff[i] * char_val(s[i])
    return check % 27

def get_decimal(dig):
    check = check_digit(dig)
    if dig[-1] != dec_to_char(check):
        return "Invalid"
    val = 0
    for c in dig[:8]:
        val = (val * 27) + char_val(c)
    return val

def main():
    P = int(input())
    for _ in range(P):
        K, digit = input().split()
        print(K, get_decimal(digit))

if __name__ == '__main__':
    main()

