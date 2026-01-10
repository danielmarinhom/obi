def is_valid_move(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == -1

def print_board(board):
    for row in board:
        print(' '.join(str(cell).zfill(2) for cell in row))

def knight_tour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), 
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    board[0][0] = 0  # Começa na posição (0, 0)
    
    if knight_tour_helper(board, 0, 0, 1, moves):
        print_board(board)
    else:
        print("No solution found.")

def knight_tour_helper(board, x, y, move_count, moves):
    if move_count == len(board) * len(board):
        return True
    
    for move in moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = move_count
            if knight_tour_helper(board, next_x, next_y, move_count + 1, moves):
                return True
            board[next_x][next_y] = -1  # Backtrack
    
    return False

# Teste
knight_tour(8)
