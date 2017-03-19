import sys

for line in sys.stdin.readlines():
    Mosq, Pup, Larv, MtoE, LtoP, PtoM, Weeks = map(int, line.split())
    stages = {'larve': Larv, 'pupae': Pup, 'adults': Mosq}
    for _  in range(Weeks):
        new_pupae = stages['larve'] // LtoP if LtoP else 0
        new_adults = stages['pupae'] // PtoM if PtoM else 0
        new_eggs = stages['adults'] * MtoE

        stages['larve'] = new_eggs
        stages['pupae'] = new_pupae
        stages['adults'] = new_adults

    print(stages['adults'])

