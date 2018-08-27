
def get_score(roll):
    if roll == [1, 2]:
        return (3, 0)
    elif roll[0] == roll[1]:
        return (2, roll[0])
    else:
        return (1, roll[1], roll[0])

line = input()
while line != "0 0 0 0":
    s0, s1, r0, r1 = map(int, line.split())
    p1 = sorted((s0, s1))
    p2 = sorted((r0, r1))

    p1_score = get_score(p1)
    p2_score = get_score(p2)

    if p1_score == p2_score:
        print("Tie.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

    line = input()
