import math
import copy
import random
from random import randrange

X = "X"
O = "O"
EMPTY = None
turn = 0

def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count =0
    o_count=0
    for i in board:
        for j in i:
            if j == X:
                x_count +=1
            if j == O:
                o_count +=1
    if x_count > o_count:
        return O
    else:
        return X


    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    x,y=0,0
    action_set =[]
    for i in board:
        for j in i:
            if j == None:
                action_set.append((x, y))
            y += 1

        x += 1
        y = 0

    return action_set
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    b = copy.deepcopy(board)
    if not (action):
        raise Exception("Invalid")
    player_trun = player(board)
    b[action[0]][action[1]]= player_trun

    return b
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """


    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        return board[1][1]
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]

    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]

    if  board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]


    if  board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    if winner(board)=="X" or winner(board) == "O":
        return True
    for i in board:
        for j in i:
            if j == None:
                return False

    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == X:
        return 1
    if won == O:
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    play=player(board)
    player_score_moves=[]
    ai_score_moves = []
    maxim=-1
    mini=1
    action=[]
    if terminal(board) :
        return None
    moves = actions(board)
    random.shuffle(moves)
    if moves.__len__() > 7:
        return moves[0]
    for i in moves:
        ai_move_board = result(board,i)
        opp_moves=actions(ai_move_board)
        for j in opp_moves:
            player_move_board =result(ai_move_board,j)
            player_score = utility(player_move_board)
            player_score_moves.append([player_score, j])
            minimax(player_move_board)
        ai_score = utility(ai_move_board)
        ai_score_moves.append([ai_score, i])
    if play == "O":
        for i,j in zip(player_score_moves,ai_score_moves):
            if j[0] == -1:
                return j[1]
            if i[0] > maxim :
                maxim =i[0]
                action=i[1]

        return action
    if play == "X":
        for i ,j in zip(player_score_moves,ai_score_moves):
            if j[0] == 1:
                return j[1]
            if i[0] < mini :
                mini =i[0]
                action=i[1]
        if action.__len__()>0:
            return action
    return moves[0]




    return moves[0]
    raise NotImplementedError
