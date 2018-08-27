N, M = map(int, input().split())
if N < M:
    print(
        'Dr. Chaz will have',
        M - N,
        'piece' + ('s' if M - N != 1 else ''),
        'of chicken left over!')
else:
    print(
        'Dr. Chaz needs',
        N - M,
        'more piece' + ('s' if N - M != 1 else ''),
        'of chicken!')