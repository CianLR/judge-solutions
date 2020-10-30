
RIGHT = {
	'South': 'East',
	'East': 'North',
	'North': 'West',
	'West': 'South',
}

FRONT = {
	'South': 'North',
	'North': 'South',
	'West': 'East',
	'East': 'West',
}

def main():
	aproach, dest, other = input().split()
	if FRONT[aproach] == dest and RIGHT[aproach] == other:
		print("Yes")
		return
	elif aproach == RIGHT[dest] and (FRONT[aproach] == other or RIGHT[aproach] == other):
		print("Yes")
		return
	print("No")

if __name__ == '__main__':
	main()