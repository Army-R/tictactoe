# Package
from abc import ABC
from abc import abstractmethod as absmet
import string
import random
from tictactoe import Cell

# Abstract class, a boilerplate for other classes
class Player(ABC):
	def __init__(self, name=None, frontend=None):
		self.name = name
		self.frontend = frontend

		@absmet
		def get_turn(self, board):
			pass

class RandomPlayer(Player):
	def __init__(self):
		random_name = "".join([random.choice(string.ascii_letters) for _ in range(8)])
		super().__init__(name=random_name)

	def get_turn(self, board):
		available_cell = []
		for i, row in enumerate(board):
			for j, column in enumerate(board):
				if board[i] [j] == Cell.EMPTY:
					cell_index = i * len(board) + j
					available_cell.append(cell_index)

		return random.choice(available_cell)

