textIn = raw_input()
changeTo = "PER"

lettersToChange = 0
for i in range(len(textIn)):
    if(textIn[i] != changeTo[i%len(changeTo)]): lettersToChange+=1

print lettersToChange

