# T = int(input())
# for _ in range(T):
#     N = int(input())


from itertools import zip_longest

class Person:
    def __init__(self, name, class_list):
        self.name = name
        class_ranks = {'upper': 2, 'middle': 1, 'lower': 0}
        self.class_list = [class_ranks[c] for c in class_list]

    def __gt__(self, other):
        paired_classes = zip_longest(
            self.class_list,
            other.class_list,
            fillvalue=1)
        for s, o in paired_classes:
            if s == o:
                continue
            return s > o
        return False

    def __lt__(self, other):
        paired_classes = zip_longest(
            self.class_list,
            other.class_list,
            fillvalue=1)
        for s, o in paired_classes:
            if s == o:
                continue
            return s < o
        return False

    def __eq__(self, other):
        return not self > other and not other > self


T = int(input())

for _ in range(T):
    N = int(input())
    # Names paired with class list, most to least significant
    people = []
    for _ in range(N):
        p = input().split()
        people.append(Person(
            name=p[0][:-1],
            class_list=p[1].split('-')[::-1]))
    sorted_people = sorted(sorted(people, key=lambda p: p.name), reverse=True)
    for p in sorted_people:
        print(p.name)
    print('='*30)
