import sys
from collections import Counter

def print_percent(trees):
    tree_counts = Counter(trees)
    num_trees = len(trees)
    for tree, count in sorted(tree_counts.items()):
        print tree, "{:.05f}".format(count * 100.0 / num_trees)

def main():
    trees = sys.stdin.read().split('\n')
    if trees[-1] == '':
        trees = trees[:-1]
    print_percent(trees)

if __name__ == '__main__':
    main()

