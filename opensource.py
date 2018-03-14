
def summarise_projects(projects):
    seen = set()
    bads = set()
    for proj in projects:
        bads |= projects[proj] & seen
        seen |= projects[proj]
    for proj in projects:
        projects[proj] -= bads
    
    for proj in sorted(projects, key=lambda x: (-len(projects[x]), x)):
        print(proj, len(projects[proj]))


def main():
    s = input()
    while s != '0':
        projects = {}
        cur_project = None
        while s != '1':
            if s.upper() == s:
                cur_project = s
                projects[s] = set()
            else:
                projects[cur_project].add(s)

            s = input()
        summarise_projects(projects)
        s = input()

if __name__ == '__main__':
    main()

