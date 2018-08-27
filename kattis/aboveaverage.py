
def main():
    T = int(raw_input())
    for _ in xrange(T):
        grades = [int(x) for x in raw_input().split()][1:]
        average = sum(grades) / float(len(grades))
        above_avg = sum(g > average for g in grades)
        print '{:.3f}%'.format(100 * above_avg / float(len(grades)))

if __name__ == '__main__':
    main()

