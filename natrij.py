curr = [int(i) for i in input().split(':')]
fut = [int(i) for i in input().split(':')]

mins_carry, sec = divmod(fut[2] - curr[2], 60)
hrs_carry, mins = divmod(mins_carry + fut[1] - curr[1], 60)
_, hrs = divmod(hrs_carry + fut[0] - curr[0], 24)

if hrs == 0 and mins == 0 and sec == 0:
    hrs = 24

print("{:02}:{:02}:{:02}".format(hrs, mins, sec))
