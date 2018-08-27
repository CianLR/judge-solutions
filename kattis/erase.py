N = int(input())
b = input()
if N % 2:
    b = ''.join(['1' if c == '0' else '0' for c in b])
if b == input():
    print("Deletion succeeded")
else:
    print("Deletion failed")
