from math import pi

R, C = map(int, input().split())

cheeze_area = (R - C) ** 2
total_area = R ** 2

print(cheeze_area * 100/total_area)
