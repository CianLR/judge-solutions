
def iprint(indent, *args, **kwargs):
    if 'end' not in kwargs:
        kwargs['end'] = ''
    print(' ' * indent, end='')
    print(*args, **kwargs)


def print_array(arr, i=0, indent=0):
    assert arr[i] == '{'
    iprint(indent, '{\n')
    i += 1
    item = ''
    while i < len(arr):
        if arr[i] == '{':
            i = print_array(arr, i, indent + 2)
        elif arr[i] == ',':
            if item:
                iprint(indent + 2, item)
                item = ''
            print(',')
        elif arr[i] == '}':
            if item:
                iprint(indent + 2, item)
            if arr[i - 1] != '{':
                print()
            break
        else:
            item += arr[i]
        i += 1
    iprint(indent, '}')
    return i

print_array(input())
print()

