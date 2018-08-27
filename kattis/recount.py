from collections import defaultdict

votes = defaultdict(int)
line = input()
while line != '***':
    votes[line] += 1
    line = input()

top_cands = sorted(votes, key=lambda k: votes[k], reverse=True)
if len(top_cands) == 1 or votes[top_cands[0]] > votes[top_cands[1]]:
    print(top_cands[0])
else:
    print("Runoff!")

