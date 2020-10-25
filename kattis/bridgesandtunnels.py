from collections import defaultdict


class UF:
	def __init__(self):
		self.parent = {}
		self.size = defaultdict(lambda: 1)

	def root(self, a):
		if a not in self.parent:
			self.parent[a] = a
			return a
		while self.parent[a] != a:
			self.parent[a] = self.parent[self.parent[a]]
			a = self.parent[a]
		return a

	def connect(self, a, b):
		ar = self.root(a)
		br = self.root(b)
		if ar == br:
			return
		if self.size[ar] > self.size[br]:
			self.parent[br] = ar
			self.size[ar] += self.size[br]
		else:
			self.parent[ar] = br
			self.size[br] += self.size[ar]

	def get_size(self, a):
		return self.size[self.root(a)]


def main():
	N = int(input())
	uf = UF()
	for _ in range(N):
		a, b = input().split()
		uf.connect(a, b)
		print(uf.get_size(a))


if __name__ == '__main__':
	main()