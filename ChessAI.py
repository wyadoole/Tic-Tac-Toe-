# 2 player tic tac toe
import itertools
from colorama import Fore, Back, Style, init
init()

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal
    for row in game:
        print(row)
        if all_same(row):
            print("Player is the winner Horizontally!(-)")
            return True

            # Diagonal
    diags = []
    for col, row, in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print("Player is the winner diagonal! (/)")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print("Player is the winner diagonal!(\)")
        return True

    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print("Player is the winner Vertically! (|)")
            return True

    return False


# win(game)


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("  0  1  2")
        if not just_display:
            game_map[row][column] = player

        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: Make your input row as 0 1 2 ?", e)

    except Exception as e:
        print("Something went very Wrong!", e)
        return False


play = True
players = [1, 2]
while play:

    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0, ]]

    game_won = False
    game = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print("player", current_player)
        column_choice = int(input("What column do you want to play? (0, 1, 2) "))
        row_choice = int(input("What row do you want to play? (0, 1, 2) "))
        game = game_board(game, current_player, row_choice, column_choice)

    if win(game):
        game_won = True
        again = input("The Game is over, would you like to play again? (y/n) ")
        if again.lower() == "y":
            print("restarting")
        elif again.lower() == "n":
            print("Bye")
            play = False
        else:
            print("Not a valid answer, so... see you later Aligator")
            play = False

game = game_board(game, just_display=True)
game = game_board(game_board, current_player, row=3, column=2)