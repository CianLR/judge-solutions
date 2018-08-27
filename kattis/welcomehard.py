
class FSM:
    def __init__(self, s):
        self.s = s
        # The number of strings up to index i, with one for '' and done
        self.stages = [0] * (len(s) + 1)
        self.stages[0] = 1  # Blank string

    def _indicies_to_update(self, char_seen):
        return [i + 1 for i, c in enumerate(self.s) if c == char_seen]


    def update_stages(self, char_seen):
        for i in self._indicies_to_update(char_seen):
            self.stages[i] += self.stages[i - 1]

    def get_possibilities(self):
        return self.stages[-1]

T = int(input())
for t in range(1, T + 1):
    m = FSM('welcome to code jam')
    for c in input():
        m.update_stages(c)
    print('Case #{}: {:04d}'.format(t, m.get_possibilities() % 10000))
