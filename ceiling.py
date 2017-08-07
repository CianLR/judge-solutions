class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Tree(object):
  def __init__(self):
    self.root = None
    self.num_nodes = 0

  def addNode(self, val):
    self.root = self._addNode(self.root, val)
    self.num_nodes += 1

  def _addNode(self, node, val):
    if node is None:
      return Node(val)
    elif val < node.val:
      node.left = self._addNode(node.left, val)
    else:
      node.right = self._addNode(node.right, val)
    return node

  def hash(self):
    if self.root is None:
      return '^'
    return self._hash(self.root)

  def _hash(self, node):
    hash_str = ''
    if node.right is not None:
      hash_str += 'R' + self._hash(node.right)
    if node.left is not None:
      hash_str += 'L' + self._hash(node.left)
    return hash_str + '^'

def main():
  n, k = map(int, raw_input().split())
  ceiling_types = set()
  for _ in xrange(n):
    bst = Tree()
    for val in map(int, raw_input().split()):
      bst.addNode(val)
    ceiling_types.add(bst.hash())
  print len(ceiling_types)

if __name__ == '__main__':
  main()

