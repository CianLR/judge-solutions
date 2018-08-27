
def product(lst):
    t = 1
    for x in lst:
        t *= x
    return t

reg = [2, 3, 5, 7, 11, 13, 17, 19]
reg_expand = [product(reg[:i]) for i in range(len(reg))]
reg_vals = [int(x) for x in input().split()]

incs_needed = 0
for i, val in reversed(list(enumerate(reg_vals))):
    incs_needed += (reg[i] - reg_vals[i] - 1) * reg_expand[i]
print(incs_needed)
