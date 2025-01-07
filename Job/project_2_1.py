"""
Project: Tic Tac Toe Game
Author: [Your name]
Email: [Your email]
Date: [Creation date]
Description: A simple Tic Tac Toe game for 2 players (Player 'O' and Player 'X')
"""

def create_board():
    """Creates an empty 3x3 game board"""
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    """Displays the current state of the game board"""
    print("\n+---+---+---+")
    for row in board:
        print(f"| {' | '.join(row)} |")
        print("+---+---+---+")

def print_rules():
    """Prints the game rules"""
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 40)
    print("Let's start the game")
    print("-" * 40)

def is_valid_move(move, board):
    """Validates if the move is legal
    
    Args:
        move (str): The player's input move
        board (list): The current game board
    
    Returns:
        bool: True if move is valid, False otherwise
    """
    if not move.isdigit():
        print("Please enter a number!")
        return False
    
    move = int(move)
    if move < 1 or move > 9:
        print("Please enter a number between 1 and 9!")
        return False
    
    row = (move - 1) // 3
    column = (move - 1) % 3
    
    if board[row][column] != " ":
        print("This position is already taken!")
        return False
        
    return True

def make_move(move, player, board):
    """Places the player's mark on the board
    
    Args:
        move (str): The validated move number
        player (str): The current player's mark ('X' or 'O')
        board (list): The game board
    """
    row = (int(move) - 1) // 3
    column = (int(move) - 1) % 3
    board[row][column] = player

def check_winner(board):
    """Checks if there's a winner
    
    Args:
        board (list): The current game board
    
    Returns:
        bool: True if there's a winner, False otherwise
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    return False

def is_draw(board):
    """Checks if the game is a draw
    
    Args:
        board (list): The current game board
    
    Returns:
        bool: True if game is a draw, False otherwise
    """
    return all(" " not in row for row in board)

def main():
    """Main game loop function"""
    board = create_board()
    current_player = "o"  # Player 'o' starts
    
    print_rules()
    display_board(board)
    
    while True:
        # Switch players
        current_player = "x" if current_player == "o" else "o"
        
        # Get valid move
        while True:
            move = input(f"Player {current_player} | Please enter your move number: ")
            if is_valid_move(move, board):
                break
        
        # Make the move
        make_move(move, current_player, board)
        display_board(board)
        
        # Check for winner
        if check_winner(board):
            print("=" * 40)
            print(f"Congratulations, the player {current_player} WON!")
            print("=" * 40)
            break
        
        # Check for draw
        if is_draw(board):
            print("=" * 40)
            print("Game over! It's a tie!")
            print("=" * 40)
            break

if __name__ == "__main__":
    main()