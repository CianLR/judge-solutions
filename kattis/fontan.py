from enum import Enum
from collections import deque

class Cell(Enum):
	WATER = 0
	AIR = 1
	STONE = 2

	@classmethod
	def to_cell(cls, c):
		if c == '.':
			return cls.AIR
		elif c == 'V':
			return cls.WATER
		return cls.STONE

	def to_string(self):
		if self == Cell.WATER:
			return 'V'
		elif self == Cell.AIR:
			return '.'
		return '#'


def simulate(N, M, grid, waters):
	q = deque(waters)
	while q:
		r, c = q.popleft()
		if r == N - 1:
			# Stop at bottom row
			continue
		beneath = grid[r + 1][c]
		if beneath == Cell.AIR:
			grid[r + 1][c] = Cell.WATER
			q.append((r + 1, c))
		elif beneath == Cell.STONE:
			if c - 1 >= 0 and grid[r][c - 1] == Cell.AIR:
				grid[r][c - 1] = Cell.WATER
				q.append((r, c - 1))
			if c + 1 < M and grid[r][c + 1] == Cell.AIR:
				grid[r][c + 1] = Cell.WATER
				q.append((r, c + 1))


def main():
	N, M = [int(x) for x in input().split()]
	waters = []
	grid = [[] for _ in range(N)]
	for row in range(N):
		for col, c in enumerate(input()):
			grid[row].append(Cell.to_cell(c))
			if grid[row][col] == Cell.WATER:
				waters.append((row, col))

	simulate(N, M, grid, waters)
	for row in grid:
		for cell in row:
			print(cell.to_string(), end='')
		print()


if __name__ == '__main__':
	main()