
possibles = {i: "single " + str(i) for i in range(1, 21)} 
possibles.update({i * 2: "double " + str(i) for i in range(1, 21)}) 
possibles.update({i * 3: "triple " + str(i) for i in range(1, 21)})

def get_throws(N):
    for v1 in possibles:
        if v1 == N:
            return [v1]
        for v2 in possibles:
            if v1 + v2 == N:
                return [v1, v2]
            if N - (v1 + v2) in possibles:
                return [v1, v2, N - (v1 + v2)]
    return None

N = int(input())
throws = get_throws(N)
if throws:
    for t in throws:
        print(possibles[t])
else:
    print("impossible")
