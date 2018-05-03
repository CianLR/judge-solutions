import sys
from bisect import insort

class Person:
    def __init__(self, name):
        self.name = name
        self.birth_date = None
        self.death_date = None
        self.decs = []
        self.ancs = []

    def __lt__(self, other):
        return self.name < other.name

    def add_birth(self, date, mother, father):
        self.birth_date = date
        self.ancs = sorted([mother, father])
        mother.add_child(self)
        father.add_child(self)

    def add_death(self, date):
        self.death_date = date

    def add_child(self, child):
        insort(self.decs, child)
    
    def format_name(self):
        fmt = self.name
        if self.birth_date:
            fmt += ' ' + self.birth_date + ' -'
        if self.death_date:
            fmt += ' ' + self.death_date
        return fmt

    def get_ancestors(self, indent=2):
        out = ''
        for parent in self.ancs:
            out += ((' ' * indent) + parent.format_name() + '\n' +
                    parent.get_ancestors(indent + 2))
        return out

    def get_descendants(self, indent=2):
        out = ''
        for child in self.decs:
            out += ((' ' * indent) + child.format_name() + '\n' +
                    child.get_descendants(indent + 2))
        return out

PEOPLE = {}
def get_person(name):
    if name not in PEOPLE:
        PEOPLE[name] = Person(name)
    return PEOPLE[name]

def main():
    lines = sys.stdin.read().strip().split('\n')
    outs = []
    for i, line in enumerate(lines):
        cmd = line.split(' ', 1)[0]
        if cmd == 'QUIT':
            break
        args = line.split(' ', 1)[1].split(' : ')
        if cmd == 'BIRTH':
            get_person(args[0]).add_birth(
                    args[1],
                    get_person(args[2]),
                    get_person(args[3]))
        elif cmd == 'DEATH':
            get_person(args[0]).add_death(args[1])
        elif cmd == 'ANCESTORS':
            outs.append("ANCESTORS of " + args[0] + '\n' + 
                        get_person(args[0]).get_ancestors())
        elif cmd == 'DESCENDANTS':
            outs.append("DESCENDANTS of " + args[0] + '\n' +
                        get_person(args[0]).get_descendants())
    print('\n'.join(outs), end='')

if __name__ == '__main__':
    main()
