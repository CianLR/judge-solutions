
def longest_prefix(a, b):
	for i, (ac, bc) in enumerate(zip(a, b)):
		if ac != bc:
			return i
	return 0

def main():
	N = int(input())
	words = sorted([input()[::-1] for _ in range(N)])
	print(max(longest_prefix(a, b) for a, b in zip(words, words[1:])))


main()