ga1, gb1, ga2, gb2 = map(int, input().split())
ea1, eb1, ea2, eb2 = map(int, input().split())

gun_sums = []
for i in range(ga1, gb1 + 1):
    for j in range(ga2, gb2 + 1):
        gun_sums.append(i + j)

pred_gun = sum(gun_sums) / len(gun_sums)

em_sums = []
for i in range(ea1, eb1 + 1):
    for j in range(ea2, eb2 + 1):
        em_sums.append(i + j)

pred_em = sum(em_sums) / len(em_sums)

if pred_em > pred_gun:
    print("Emma")
elif pred_em < pred_gun:
    print("Gunnar")
else:
    print("Tie")
