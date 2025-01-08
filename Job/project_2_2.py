"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
"""

# Import only necessary libraries
from colorama import Fore, Style, init  # For colorizing output (optional, for better UX)

# Initialize colorama (optional)
init(autoreset=True)

# Constants for the game
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_CELL = " "

# Display welcome message and rules
def display_welcome():
    print(Fore.CYAN + "Welcome to Tic Tac Toe")
    print(Fore.CYAN + "=" * 40)
    print(Fore.MAGENTA + "GAME RULES:")
    print(Fore.WHITE + "Each player can place one mark (X or O)")
    print("The " + Fore.GREEN + "WINNER " + Fore.WHITE + "is the one who succeeds in placing three of their marks in a:")
    print(Fore.YELLOW + "* Horizontal row")
    print(Fore.YELLOW + "* Vertical row")
    print(Fore.YELLOW + "* Diagonal row")
    print(Fore.CYAN + "=" * 40)
    print(Fore.LIGHTBLUE_EX + "Let's start the game!\n")

# Initialize the game board
def initialize_board():
    return [EMPTY_CELL] * 9

# Display the game board
def display_board(board):
    print(Fore.YELLOW + "+---+---+---+")
    for i in range(0, 9, 3):
        print(Fore.YELLOW + f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print(Fore.YELLOW + "+---+---+---+")

# Check if a move is valid
def is_valid_move(board, move):
    return move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == EMPTY_CELL

# Place the player's mark on the board
def place_move(board, move, player):
    board[int(move) - 1] = player

# Check for a win condition
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check for a draw
def check_draw(board):
    return all(cell != EMPTY_CELL for cell in board)

# Main game loop
def play_game():
    display_welcome()
    board = initialize_board()
    current_player = PLAYER_X

    while True:
        display_board(board)
        move = input(f"Player {Fore.GREEN + current_player}{Style.RESET_ALL}, enter your move (1-9): ")

        if not is_valid_move(board, move):
            print(Fore.RED + "Invalid move. Please try again.")
            continue

        place_move(board, move, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print(Fore.GREEN + f"Congratulations! Player {current_player} wins!")
            break

        if check_draw(board):
            display_board(board)
            print(Fore.YELLOW + "It's a draw!")
            break

        # Switch player
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

# Run the game
if __name__ == "__main__":
    play_game()
