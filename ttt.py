# one player tic tac toe with AI or player vs AI

# Video post for presintations: https://youtu.be/rbBJnEX7pfk

from random import randint
import os

class AI:
    def __init__(self, board):
        self.board = board

        self.piece = 'O'

    def calc_move(self):
        available_coords = []

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (self.board[i][j] == ' '):
                    available_coords.append([i, j])

        rand_coord = available_coords[randint(0, len(available_coords)-1)]

        self.board[rand_coord[1]][rand_coord[0]] = 'O'

game = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' '],]

def print_board(board):
    print("\t 0 1 2")
    count = 0
    for row in board:
        print(count, end='\t')
        for col in row:
            print('|' + col, end='')
        print('|')
        count = count + 1

def get_input():
    user_input = input("Please enter the coordinates of the position you want to place at as a comma separated list (x, y): ")

    while len(user_input) > 3:
        user_input = input("Too many characters. Please enter as a comma separated list ('x, y'): ")

    while (user_input[0] not in '012' and user_input[2] not in '012'):
        user_input = input("Invalid input. Please enter as a comma separated list ('x, y'): ")


    return [int(user_input[0]), int(user_input[2])]

def check_game_over(board):
    cols = [[],
            [],
            []]

    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return True
        else:
            cols[0].append(row[0])
            cols[1].append(row[1])
            cols[2].append(row[2])

    for col in cols:
        if len(set(col)) == 1 and col[0] != ' ':
            return True

    diag_1 = [board[0][0], board[1][1], board[2][2]]
    diag_2 = [board[0][2], board[1][1], board[2][0]]

    if (len(set(diag_1)) == 1 and diag_1[0] != ' ') or (len(set(diag_2)) == 1 and diag_2[0] != ' '):
        return True

    return False

def main():
    global game

    playerScore = 0
    aiScore = 0

    game_over = False

    ai = AI(game)

    while (not game_over):
        print_board(game)

        game_over = check_game_over(game)
        if not game_over:
            inputs = get_input()

            game[inputs[1]][inputs[0]] = 'X'
            ai.calc_move()

            os.system('cls')







if __name__ == '__main__':
    main()