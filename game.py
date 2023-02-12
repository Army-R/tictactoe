# Create a Game class to represent the Tic Tac Toe python game

class Game(object):
	def __init__(self):
		# Board and 2 players
		self.board = [
		[Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
		[Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
		[Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
		]
		
		# is_x_turn boolean field keep track of alternating turns between players
		self.is_x_tunr = True
		self.x_player = x_player
		self.o_player = o_player

	def _check_draw(self):
		for row in self.board:
			for cell in row:
				if cell == Cell.EMPTY:
					return False
		return True


	def _check_winner(self):
		# Check rows
		for row in self.board:
			if len(set(row)) == 1 and row[0] != Cell.EMPTY:
				return row[0]

		# Check columns
		for col in [*zip(self.board)]:
			if len(set(col)) == 1 col[0] != Cell.EMPTY:
				return col[0]

		# Check diagonals
		size = len(self.board)
		major_diag = set()
		minor_diag = set()
		for i in rage(size):
			major_diag.add(self.board[i] [i])
			minor_diag.add(self.board[i] [size-i-1])

	

	def make_turn(self):
		pass

	def print_board(self):
		pass

	def is_game_over(slef):
		winner = self._check_winner()
		if winner is not None:
			return winner 

		return self._check_draw()

	def print_winner(self):
		pass

	# Defines the flow for the game
	def play(self):
		self.print_board()
		while not (winner := self.is_game_over()):
			if self.is_x_tunr:
				turn = self.x_player.get_turn(self.board)
				pice = Cell.X 
			else:
				turn = self.o_player.get_turn(self.board)
				pice = Cell.O 
			self.make_turn(turn, pice)
			self.print_board()
		self.print_winner(winner)