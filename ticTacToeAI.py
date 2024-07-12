import random

def get_optimal_move(board):
    def check_winner(board, player):
        for row in board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True

        if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
            return True

        return False

    def available_moves(board):
        return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

    def minimax(board, depth, maximizing_player):
        if check_winner(board, 'X'):
            return -10 + depth
        elif check_winner(board, 'O'):
            return 10 - depth
        elif len(available_moves(board)) == 0:
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for move in available_moves(board):
                board[move[0]][move[1]] = 'O'
                eval = minimax(board, depth + 1, False)
                max_eval = max(max_eval, eval)
                board[move[0]][move[1]] = ' '
            return max_eval
        else:
            min_eval = float('inf')
            for move in available_moves(board):
                board[move[0]][move[1]] = 'X'
                eval = minimax(board, depth + 1, True)
                min_eval = min(min_eval, eval)
                board[move[0]][move[1]] = ' '
            return min_eval

    def find_best_move(board):
        best_move = None
        best_eval = float('-inf')
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, 0, False)
            board[move[0]][move[1]] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move

    return find_best_move(board)

def return_best_move(board):

    random_number = random.choice([1, 2, 3, 4, 5])

    empty_board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    if (board == empty_board):
        if random_number == 1:
            optimal_move = (1,1)
        elif random_number == 2:
            optimal_move = (0,0)
        elif random_number == 3:
            optimal_move = (2,2)
        elif random_number == 4:
            optimal_move = (2,0)
        else:
            optimal_move = (0,2)
    else:
        optimal_move = get_optimal_move(board)
    return optimal_move
