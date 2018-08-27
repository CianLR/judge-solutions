from datetime import date

D, M = map(int, input().split())

d = date(2009, M, D)
print(d.strftime("%A"))
