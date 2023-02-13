# Packages
from tictactoe.game import Game
from tictactoe.player import RandomPlayer

# Main function
def main():
	x_player = RandomPlayer()
	o_player = RandomPlayer()
	game = Game(x_player=x_player, o_player=o_player)
	game.play()

if __name__ == "__main__":
	main()