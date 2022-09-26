"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if sum(i.count(X) for i in board) > sum(i.count(O) for i in board):
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilities = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibilities.add((i, j))
    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][0] == board [0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board [1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board [2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] and board[0][0] == board [2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[0][1] == board [2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[0][2] == board [2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[0][0] == board [2][2]:
        return board[0][0]
    elif board[2][0] == board[1][1] and board[2][0] == board [0][2]:
        return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None
    value = -2
    move = None

    for action in actions(board):
        v, m = min_value(result(board, action))
        if v > value:
            value = v
            move = action
            if value == 1:
                return value, move
    return value, move


def min_value(board):
    if terminal(board):
        return utility(board), None
    value = 2
    move = None

    for action in actions(board):
        v, m = max_value(result(board, action))
        if v < value:
            value = v
            move = action
            if value == -1:
                return value, move
    return value, move