
def product(lst):
    tot = 1
    for n in lst:
        tot *= n
    return tot

long_to_short = {
    'thou': 'th',
    'inch': 'in',
    'foot': 'ft',
    'yard': 'yd',
    'chain': 'ch',
    'furlong': 'fur',
    'mile': 'mi',
    'league': 'lea'
}

# Unit N expressed as number of unit N-1's
ratios = [1000, 12, 3, 22, 10, 8, 3]
short_to_th = {
    u: product(ratios[:i]) for i, u in enumerate(
        ['th', 'in', 'ft', 'yd', 'ch', 'fur', 'mi', 'lea'])
}

in_int, from_u, _, to_u = input().split()
if from_u in long_to_short:
    from_u = long_to_short[from_u]
if to_u in long_to_short:
    to_u = long_to_short[to_u]

in_int_thou = int(in_int) * short_to_th[from_u]
print(in_int_thou / short_to_th[to_u])
