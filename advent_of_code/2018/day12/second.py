import sys

def hedge_to_bin(h):
    return int(''.join('0' if c == '.' else '1' for c in h), 2)

def next_state(match, state, z):
    MASK = (2 ** 5) - 1
    while not state.startswith('.....'):
        z += 1
        state = '.' + state
    for i in xrange(len(state)):
        if state[i] != '.':
            if i > 5:
                rm = i - 5
                z -= rm
                state = state[rm:]
            break
    while not state.endswith('.....'):
        state += '.'
    bit = 0
    new_state = ['.', '.']
    for i in xrange(2, len(state) - 2):
        bit = ((bit << 1) & MASK) | (state[i + 2] == '#')
        new_state.append('#' if match[bit] else '.')
    ns = ''.join(new_state) + '..'
    return z, ns

def iter_states(match, state, iters):
    z = 0
    for i in xrange(iters):
        nz, nstate = next_state(match, state, z)
        if nstate == state:
            iters_left = (iters - 1) - i
            return (nz + ((nz - z) * iters_left)), state
        z, state = nz, nstate
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
    z, state = iter_states(match, state, 50000000000)
    print get_state_value(state, z)

if __name__ == '__main__':
    main()

