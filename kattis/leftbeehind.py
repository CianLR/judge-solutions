sweet, sour = map(int, input().split())

while sweet or sour:
    if sweet + sour == 13:
        print("Never speak again.")
    elif sweet == sour:
        print("Undecided.")
    elif sweet > sour:
        print("To the convention.")
    else:
        print("Left beehind.")

    sweet, sour = map(int, input().split())
