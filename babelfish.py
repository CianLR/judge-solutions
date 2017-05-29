import sys

lines = sys.stdin.readlines()
l = 0

for_to_eng = {}
while lines[l] != '\n':
    eng, fr = lines[l].split()
    for_to_eng[fr] = eng
    l += 1

l += 1

while l < len(lines):
    line = lines[l].strip()
    print(for_to_eng[line] if line in for_to_eng else 'eh')
    l += 1
