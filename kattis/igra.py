from collections import OrderedDict, defaultdict

class GameLetters:
	def __init__(self, s):
		self.s = s
		self.avail_chars = [True] * len(s)
		self.right_i = len(s) - 1
		char_locations = defaultdict(list)
		for i, c in enumerate(s):
			char_locations[c].append(i)
		self.char_locs = OrderedDict(
			sorted(char_locations.items()))

	def remove_letter(self, i):
		self.avail_chars[i] = False
		c = self.s[i]
		self.char_locs[c].pop()
		if not self.char_locs[c]:
			del self.char_locs[c]

	def get_alpha(self):
		if not self.char_locs:
			return None
		c = next(iter(self.char_locs))
		self.remove_letter(self.char_locs[c][-1])
		return c

	def get_right(self):
		while self.right_i >= 0 and not self.avail_chars[self.right_i]:
			self.right_i -= 1
		if self.right_i < 0:
			return None
		self.remove_letter(self.right_i)
		self.right_i -= 1
		return self.s[self.right_i + 1]



def main():
	N = int(input())
	s = input()
	gl = GameLetters(s)
	a, b = '', ''
	for _ in range(N//2):
		a += gl.get_right()
		b += gl.get_alpha()
	if b < a:
		print("DA")
	else:
		print("NE")
	print(b)


if __name__ == '__main__':
	main()