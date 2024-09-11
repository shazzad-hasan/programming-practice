import numpy as np
import random

# create an empty 3 x 3 board
def create_board():
    return np.zeros((3,3))

# available places on the board
def empty_places(board):
    available_places = []
    board_length = len(board)
    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] == 0:
                available_places.append((i,j))
    return available_places

# select a random place for the player
def player_turn(board, player):
    available_spaces = empty_places(board)
    random_location = random.choice(available_spaces)
    board[random_location] = player
    return board

# check horizontal winner
def horizontal_win(board, player):
    rows = len(board)
    columns = rows
    
    for r in range(rows):
        win = True
        for c in range(columns):
            if board[r][c] != player:
                win = False
        if win == True:
            break 
    return win

# check vertical winner
def vertical_win(board, player):
    rows = len(board)
    columns = rows
    
    for r in range(rows):
        win = True
        for c in range(columns):
            if board[c][r] != player:
                win = False
        if win == True:
            break 
    return win

# check diagonal winner
def diagonal_win(board, player):
    board_length = len(board)
    
    win = True
    for i in range(board_length):
        if board[i][i] != player:
            win = False
    if win == True:
        return True
    
    # check other diagonal
    win = True 
    for i in range(board_length):
        j = board_length - i - 1
        if board[i,j] != player:
            win = False
    return win
    
# evaluate the board
def evaluate_board(board):
    winner = None
    for player in [1, 2]:
        if (horizontal_win(board, player) or vertical_win(board, player) or diagonal_win(board, player)):
            winner = player
    return winner
    

# play the game
def play():
    board = create_board()
    winner = None
    count = 1
    
    while count <= 9:
        for player in [1, 2]:
            current_board = player_turn(board, player)
            print("Board position after " + str(count) + " move")
            print(current_board)
            count += 1
            winner = evaluate_board(current_board)
            if winner in [1,2]:
                return winner
            if count > 9:
                winner = -1
                return winner

    return winner
    
print("The winner is: " + str(play()))
