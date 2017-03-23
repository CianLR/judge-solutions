T = int(input())
for tc in range(1, T + 1):
    print("Recipe #", tc)
    R, P, D = map(int, input().split())
    ingrd = []
    main_weight_scaled = -1
    for _ in range(R):
        name, w, per = input().split()
        ingrd.append((name, float(w), float(per)/100))
        if per == '100.0':
            main_weight_scaled = (D / P) * float(w)
    for name, w, per in ingrd:
        print(name, '{:.1f}'.format(round(per * main_weight_scaled, 1)))
    print('----------------------------------------')
