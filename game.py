from board import initialize_board, print_board
from player import ask_for_player_move, is_valid_move, update_game_board

def check_for_win(board):
    """Checks if there is a winning condition on the board."""
    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":  # Row
            return True
        if board[0][i] == board[1][i] == board[2][i] != "-":  # Column
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-" or board[0][2] == board[1][1] == board[2][0] != "-":  # Diagonals
        return True
    return False


def play_game():
   board= initialize_board()
   current_player = 'X'
   for _ in range(9):
      print_board(board)
      print(f"Player {current_player}, it's your turn.")
      valid_move = False
      while not valid_move:
        row, col = ask_for_player_move()
        if is_valid_move(board, row, col):
            update_game_board(board, row, col, current_player)
            if check_for_win(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                exit()
            valid_move = True
        else:
            print("Invalid move. Try again.")

    
        current_player = 'O' if current_player == 'X' else 'X'
      print_board(board)
     
