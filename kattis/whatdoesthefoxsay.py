T = int(input())
for _ in range(T):
    sounds = input().split()
    ani = input()
    while '?' not in ani:
        for sound in ani.split()[2:]:
            while sound in sounds:
                sounds.remove(sound)
        ani = input()
    print(*sounds)
