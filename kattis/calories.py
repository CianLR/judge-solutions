from math import floor

def real_round(x):
    return int(floor(x + 0.5))

C_PER_G = [9, 4, 4, 4, 7]

line = input()
while line != '-':
    tot_cals = 0
    cals_from_fat = 0
    while line != '-':
        food_calories = [0, 0, 0, 0, 0]
        food_percent = [0, 0, 0, 0, 0]
        for i, amt in enumerate(line.split()):
            val, typ = int(amt[:-1]), amt[-1]
            if typ == 'g':
                food_calories[i] += val * C_PER_G[i]
            elif typ == '%':
                food_percent[i] += val / 100
            elif typ == 'C':
                food_calories[i] += val
        tot_line_cals = sum(food_calories) / (1 - sum(food_percent))
        tot_cals += tot_line_cals
        cals_from_fat += food_calories[0] + (food_percent[0] * tot_line_cals)
        line = input()

    print("{}%".format(real_round(cals_from_fat * 100/ tot_cals)))

    line = input()
