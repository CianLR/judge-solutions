
class LRUCache:
  class Node:
    def __init__(self, k, v):
     self.k = k
     self.v = v
     self.next = None
     self.prev = None

  def __init__(self, capacity: int):
    self.cap = capacity
    self.head = None
    self.tail = None
    self.lookup = {}
  
  def pop_key(self, key):
    n = self.lookup[key]
    if n.next:
      n.next.prev = n.prev
    if n.prev:
      n.prev.next = n.next
    if n is self.head:
      self.head = n.next
    if n is self.tail:
      self.tail = n.prev
    n.next = None
    n.prev = None
    return n

  def make_head(self, n):
    n.next = self.head
    if self.head:
      self.head.prev = n
    self.head = n
    if self.tail is None:
      self.tail = n
  
  def pop_tail(self):
    n = self.tail
    self.lookup.pop(n.k)
    if n.prev:
      n.prev.next = None
    self.tail = n.prev
    if n is self.head:
      self.head = None
    del n

  def get(self, key: int) -> int:
    if key not in self.lookup:
      return -1
    n = self.pop_key(key)
    self.make_head(n)
    return n.v

  def put(self, key: int, value: int) -> None:
    if key in self.lookup:
      self.pop_key(key)
    if len(self.lookup) == self.cap:
      self.pop_tail()
    n = LRUCache.Node(key, value)
    self.make_head(n)
    self.lookup[key] = n


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
