"""
Tic Tac Toe Player
"""


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
    x_steps = 0
    o_steps = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_steps += 1
            if cell == O:
                o_steps += 1
                    
    if x_steps > o_steps:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    
    if board[i][j] != EMPTY:
        raise IndexError("invalid action")

    result = copy.deepcopy(board)
    next_player = player(result)
    result[i][j] = next_player
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_conditions = [
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],
        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1,2], [2,2]],
        [[0,0], [1,1], [2,2]],
        [[2,0], [1,1], [0,2]],
        ]
    for row in winning_conditions:
        if board[row[0][0]][row[0][1]] == X and board[row[1][0]][row[1][1]] == X and board[row[2][0]][row[2][1]] == X:
            return X
            break
        if board[row[0][0]][row[0][1]] == O and board[row[1][0]][row[1][1]] == O and board[row[2][0]][row[2][1]] == O:
            return O
            break
        
    return None
        
            
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    
    if winner(board) == None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        isMaximizing = True
    else:
        isMaximizing = False
        
    if terminal(board):
        return None
    
    possible_moves = actions(board)
    if isMaximizing:
        best_score = -1000
        for move in possible_moves:
            next_state = result(board, move)
            score = minimax_scoring(next_state, 0, not isMaximizing)
            if score > best_score:
                print("maximizing score, best score", score, best_score, move)
                best_score = score
                best_move = move
        
    else:
        best_score = 1000
        for move in possible_moves:
            next_state = result(board, move)
            score = minimax_scoring(next_state, 0, not isMaximizing)
            if score < best_score:
                print("minimizing score, best score", score, best_score, move)
                best_score = score
                best_move = move
                
    return best_move

def minimax_scoring(board, depth, isMaximizing):
    if terminal(board):
        return utility(board)
    possible_moves = actions(board)
    if isMaximizing:
        best_score = -1000
        for move in possible_moves:
            next_state = result(board, move)
            score = minimax_scoring(next_state, depth +1, False)
            best_score = max(score, best_score)
           

    else:
        best_score = 1000
        for move in possible_moves:
            next_state = result(board, move)
            score = minimax_scoring(next_state, depth +1, True)
            best_score = min(score, best_score)
    return best_score        



