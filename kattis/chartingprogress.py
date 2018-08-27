from sys import stdin

def print_table(log):
    # ['..*', '*..', '.*.']
    width = len(log[0])
    records_printed = 0
    for line in log:
        stars = line.count('*')
        print(('.' * (width - stars - records_printed)) +
              ('*' * stars) +
              ('.' * (records_printed)))
        records_printed += stars
    print()


def main():
    logs = stdin.read().split('\n\n')
    for log in logs:
        print_table(log.strip().split('\n'))



if __name__ == '__main__':
    main()

