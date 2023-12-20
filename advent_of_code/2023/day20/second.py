import sys, heapq
from collections import namedtuple, defaultdict, deque

LOW_PULSE = 0
HIGH_PULSE = 1

class BroadcastNode:
  def __init__(self):
    self.inputs = []
    self.outputs = []
  
  def pulse(self, prev, pulse):
    return pulse, self.outputs

class FlipFlopNode:
  def __init__(self):
    self.inputs = []
    self.outputs = []
    self.on = False

  def pulse(self, prev, pulse):
    if pulse == HIGH_PULSE:
      return None, []
    self.on = not self.on
    if self.on:
      return HIGH_PULSE, self.outputs
    return LOW_PULSE, self.outputs

class ConjunctionNode:
  def __init__(self):
    self.inputs = []
    self.outputs = []
    self.last_pulse = {}

  def all_inputs_high(self):
    return all(self.last_pulse.get(n, LOW_PULSE) == HIGH_PULSE for n in self.inputs)

  def pulse(self, prev, pulse):
    self.last_pulse[prev] = pulse
    if self.all_inputs_high():
      return LOW_PULSE, self.outputs
    return HIGH_PULSE, self.outputs

class NopNode:
  def __init__(self):
    self.inputs = []
    self.outputs = []

  def pulse(self, prev, pulse):
    return None, []

class Graph:
  def __init__(self):
    self.nodes = {}
  
  def print(self):
    for name, n in self.nodes.items():
      print(name, n.__class__.__name__, "in (", n.inputs, ') out (', n.outputs, ')')

  def add_node(self, definition):
    if definition[0] == '%':
      self.nodes[definition[1:]] = FlipFlopNode()
    elif definition[0] == '&':
      self.nodes[definition[1:]] = ConjunctionNode()
    else:
      self.nodes[definition] = BroadcastNode()
  
  def add_connection(self, name, outputs):
    self.nodes[name].outputs = outputs
    for o in outputs:
      if o not in self.nodes:
        self.nodes[o] = NopNode()
      self.nodes[o].inputs.append(name)
  
  def start_pulse(self, node, pulse, prev='button'):
    counts = defaultdict(lambda: [0, 0])
    q = deque([(node, pulse, prev)])
    while q:
      n, p, pr = q.popleft()
      counts[n][p] += 1
      outp, outns = self.nodes[n].pulse(pr, p)
      q.extend((o, outp, n) for o in outns)
    return counts

def build_graph(lines):
  g = Graph()
  names = []
  outputs = []
  for line in lines:
    name, outs = line.split(' -> ')
    g.add_node(name)
    names.append(name)
    outputs.append(outs.split(', '))
  for name, outs in zip(names, outputs):
    if name[0] in '&%':
      name = name[1:]
    g.add_connection(name, outs)
  return g

def main():
  sys.setrecursionlimit(100000)
  lines = sys.stdin.read().split('\n')
  graph = build_graph(lines)

  factors = {}
  feed_nodes = {'kl', 'vm', 'kv', 'vb'}
  button_presses = 0
  while feed_nodes:
    button_presses += 1
    counts = graph.start_pulse('broadcaster', LOW_PULSE)
    for fn in list(feed_nodes):
      if counts[fn][LOW_PULSE] > 0:
        factors[fn] = button_presses
        feed_nodes.remove(fn)

  # Only works because they are prime
  a = 1
  for f in factors.values():
    a *= f
  print(a)

if __name__ == '__main__':
  main()