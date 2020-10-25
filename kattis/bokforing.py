

class Comp:
	def __init__(self, N):
		self.wealth = [0] * N
		self.last_set = [-1] * N
		self.last_reset_time = -1
		self.last_reset_amount = 0
		self.command_index = 0
		self.commands = {
			'SET': self.command_set,
			'PRINT': self.command_print,
			'RESTART': self.command_restart,
		}

	def run(self, statement):
		command, *args = statement.split()
		self.commands[command](*map(int, args))
		self.command_index += 1

	def command_set(self, person, amount):
		self.wealth[person - 1] = amount
		self.last_set[person - 1] = self.command_index

	def command_print(self, person):
		amount = -1
		if self.last_set[person - 1] > self.last_reset_time:
			amount = self.wealth[person - 1]
		else:
			amount = self.last_reset_amount
		print(amount)

	def command_restart(self, amount):
		self.last_reset_time = self.command_index
		self.last_reset_amount = amount


def main():
	N, Q = [int(x) for x in input().split()]
	comp = Comp(N)
	for _ in range(Q):
		comp.run(input())


if __name__ == '__main__':
	main()