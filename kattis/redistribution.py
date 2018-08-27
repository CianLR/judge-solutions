N = int(input())
students = [int(x) for x in input().split()]

if max(students) * 2 > sum(students):
    print("impossible")
else:
    studs_w_indicies = [(s, i + 1) for i, s in enumerate(students)]
    studs_w_indicies = sorted(studs_w_indicies, reverse=True)
    print(*[x[1] for x in studs_w_indicies])
