N = int(input())
for _ in range(N):
    cmd = input()
    if cmd.startswith('simon says'):
        print(cmd[11:])