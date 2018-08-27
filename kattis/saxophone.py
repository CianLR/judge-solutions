
note_to_fingers = {
    'c': (2, 3, 4, 7, 8, 9, 10),
    'd': (2, 3, 4, 7, 8, 9),
    'e': (2, 3, 4, 7, 8),
    'f': (2, 3, 4, 7),
    'g': (2, 3, 4),
    'a': (2, 3),
    'b': (2,),
    'C': (3,),
    'D': (1, 2, 3, 4, 7, 8, 9),
    'E': (1, 2, 3, 4, 7, 8),
    'F': (1, 2, 3, 4, 7),
    'G': (1, 2, 3, 4),
    'A': (1, 2, 3),
    'B': (1, 2),
}

T = int(input())
for _ in range(T):
    notes = input()

    press_count = {i:0 for i in range(1, 11)}
    last_fingers = ()
    for n in notes:
        for fing in note_to_fingers[n]:
            if fing not in last_fingers:
                press_count[fing] += 1
        last_fingers = note_to_fingers[n]
    print(*press_count.values())
