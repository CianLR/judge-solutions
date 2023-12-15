import sys
from collections import defaultdict

def HASH(s):
  v = 0
  for c in s:
    v = ((ord(c) + v) * 17) % 256
  return v

class HASHMAP:
  def __init__(self):
    self.boxes = [{} for _ in range(256)]
    self.box_order = [[] for _ in range(256)]

  def remove(self, k):
    h = HASH(k)
    d = self.boxes[h]
    if k in d:
      del d[k]
  
  def add(self, k, v):
    h = HASH(k)
    self.boxes[h][k] = v
  
  def apply_step(self, step):
    if step.endswith('-'):
      self.remove(step[:-1])
    else:
      k, v = step.split('=')
      self.add(k, int(v))
    # print("After", step)
    # self.print()
  
  def print(self):
    for box_n, box in enumerate(self.boxes):
      if len(box) == 0: continue
      print("Box", box_n, end=": ")
      for slot_n, (lens, focal) in enumerate(box.items()):
        print(f"[{lens} {focal}]", end=" ")
      print()
  
  def power(self):
    pw = 0
    for box_n, box in enumerate(self.boxes):
      for slot_n, (lens, focal) in enumerate(box.items()):
        # print(lens, box_n + 1, slot_n + 1, focal)
        pw += (box_n + 1) * (slot_n + 1) * focal
    return pw

def main():
  seq = input().split(',')
  hm = HASHMAP()
  for part in seq:
    hm.apply_step(part)
  print(hm.power())

if __name__ == '__main__':
  main()