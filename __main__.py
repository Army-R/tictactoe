# Module
from tictactoe.game import Game
from tictactoe.player import ConsolePlayer
from tictactoe.io import ConsoleFrontend
from tictactoe.io import TableConsoleFrontend


# Main function
def main():
    frontend = ConsoleFrontend()
    # frontend = TableConsoleFrontend()
    player = ConsolePlayer('Army')
    game = Game(x_player=player, frontend=frontend)
    game.play()


if __name__ == '__main__':
    main()
