N, *inds = map(int, input().split())
while N != 0:
    message = input()
    if len(message) % N:
        message += ' ' * (N - (len(message) % N))
    inds = [x - 1 for x in inds]
    enc = [''] * len(message)
    for i in range(len(message)):
        enc_letter_i = ((i // N) * N) + inds[i % N]
        enc[i] = message[enc_letter_i]
    print("'" + ''.join(enc) + "'")

    N, *inds = map(int, input().split())
