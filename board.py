def initialize_board():
    """Creates an empty 3x3 Tic Tac Toe board."""
    board = []
    for _ in range(3):
        board.append(["-" for _ in range(3)])  # Fixed board initialization
    return board

def print_board(board):
    """Prints the game board."""
    print("Current game board:")
    for row in board:
        print(" | ".join(row))
    print()



 
