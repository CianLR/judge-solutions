a, b, c = input().split()

for op in ['+', '-', '/', '*']:
    expr = a + op + b + '=' + c
    exec('is_valid = ' + expr.replace('=', '=='))
    if is_valid:
        print(expr)
        break

    expr = a + '=' + b + op + c
    exec('is_valid = ' + expr.replace('=', '=='))
    if is_valid:
        print(expr)
        break

