
def push(stack):
    stack.append(frozenset())

def dup(stack):
    stack.append(stack[-1])

def union(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a | b)

def intersect(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a & b)

def add(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b | { hash(a) })

OPS = {
    'PUSH': push,
    'DUP': dup,
    'UNION': union,
    'INTERSECT': intersect,
    'ADD': add,
}

T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    stack = []
    for _ in xrange(N):
        OPS[raw_input()](stack)
        print len(stack[-1])
    print '***'
