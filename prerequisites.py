
class Category:
    def __init__(self, reqs, contains):
        self.reqs = int(reqs)
        self.contains = set(contains)

def main():
    f = input()
    while f != '0':
        ncourse, cats = map(int, f.split())
        categories = []
        courses = set(input().split())
        for _ in range(cats):
            _, req, *contains = input().split()
            categories.append(Category(req, contains))

        for c in categories:
            if len(c.contains & courses) < c.reqs:
                print("no")
                break
        else:
            print("yes")

        f = input()

if __name__ == '__main__':
    main()

