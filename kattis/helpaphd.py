
N = int(input())
for _ in range(N):
    prob = input()
    if prob == "P=NP":
        print("skipped")
    else:
        print(eval(prob))

