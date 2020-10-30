
def main():
	N = int(input())
	bricks = [int(x) for x in input().split()]
	towers = 0
	last_b = 0
	for b in bricks:
		if b > last_b:
			towers += 1
		last_b = b
	print(towers)

if __name__ == '__main__':
	main()