import sys

def hedge_to_bin(h):
    return int(''.join('0' if c == '.' else '1' for c in h), 2)

def next_state(match, state, z):
    MASK = (2 ** 5) - 1
    while not state.startswith('.....'):
        z += 1
        state = '.' + state
    while not state.endswith('.....'):
        state += '.'
    bit = 0
    new_state = ['.', '.']
    for i in xrange(2, len(state) - 2):
        bit = ((bit << 1) & MASK) | (state[i + 2] == '#')
        new_state.append('#' if match[bit] else '.')
    return z, ''.join(new_state) + '.'

def iter_states(match, state, iters):
    z = 0
    for _ in xrange(iters):
        z, state = next_state(match, state, z)
    return z, state

def get_state_value(state, z):
    s = 0
    for i, c in enumerate(state):
        if c == '#':
            s += i - z
    return s

def main():
    state = sys.stdin.readline()[len('initial state: '):].strip()
    assert sys.stdin.readline() == '\n'
    match = [False] * (2 ** 5)
    for line in sys.stdin.readlines():
        s, _, to = line.split()
        match[hedge_to_bin(s)] = to == '#'
    z, state = iter_states(match, state, 20)
    print get_state_value(state, z)

if __name__ == '__main__':
    main()

