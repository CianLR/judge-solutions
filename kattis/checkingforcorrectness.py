from sys import stdin

MOD = 10000

OPS = {
    '+': (lambda a, b: (a + b) % MOD),
    '*': (lambda a, b: (a * b) % MOD),
    '^': (lambda a, b: pow(a, b, MOD)),
}

def main():
    for line in stdin.readlines():
        a, op, b = line.split()
        print(OPS[op](int(a), int(b)))

if __name__ == '__main__':
    main()

