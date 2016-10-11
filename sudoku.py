#!/usr/bin/python3

board = []
for x in range(0, 9):
    board.append(["O"] * 9)

def print_board(board):
    for row in board:
        print("|".join(row))

print_board(board)