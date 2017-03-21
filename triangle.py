import sys
from math import log, floor

for case, i in enumerate(map(int, sys.stdin.readlines())):
    perim = log(3, 10) + (i * log(1.5, 10))
    print('Case ' + str(case + 1) + ':', floor(perim + 1))
