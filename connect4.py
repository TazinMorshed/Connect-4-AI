from tkinter.tix import ROW
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece
    pass


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_baord(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # check all the horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # check vertical locatons


board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = input("Player 1 Make your selection (0-6)")
        col = int(col)

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("player 1 Wins")
                game_over = True

    # Ask for player 2 input
    else:
        col = input("Player 2 Make your selection (0-6)")
        col = int(col)

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    print_baord(board)
    turn += 1
    turn = turn % 2
