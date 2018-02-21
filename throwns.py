
class Command:
    def __init__(self, n, v):
        self.n = n
        self.v = v

    def exec(self, states):
        raise NotImplemented()

class UndoCommand(Command):
    def exec(self, states):
        for _ in range(self.v):
            states.pop()

class PassCommand(Command):
    def exec(self, states):
        states.append((states[-1] + self.v) % self.n)


def parse_commands(N, K):
    commands = []
    cmds = input().split()
    cmd_i = 0
    for _ in range(K):
        if cmds[cmd_i] == 'undo':
            commands.append(UndoCommand(N, int(cmds[cmd_i + 1])))
            cmd_i += 2
        else:
            commands.append(PassCommand(N, int(cmds[cmd_i])))
            cmd_i += 1
    return commands

def get_final_state(commands):
    states = [0]
    for cmd in commands:
        cmd.exec(states)
    return states[-1]

def main():
    N, K = map(int, input().split())
    commands = parse_commands(N, K)
    print(get_final_state(commands))

if __name__ == '__main__':
    main()

