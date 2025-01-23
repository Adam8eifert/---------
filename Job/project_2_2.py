"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Adam Seifert
email: seifert.promotion@gmail.com
"""

# Import libraries
from colorama import Fore, init  

# Initialize colorama (optional)
init(autoreset=True)

# Constants 
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_CELL = " "
SEPARATOR = (f"{Fore.CYAN}{'=' * 40}")

# Display welcome message and rules
def display_welcome():
    print(f"{Fore.BLUE}Welcome to Tic Tac Toe")
    print(SEPARATOR)
    print(f"{Fore.MAGENTA}GAME RULES:")
    print(f"{Fore.WHITE}Each player can place one mark ({Fore.RED}X{Fore.WHITE} or {Fore.BLUE}O{Fore.WHITE})")
    print(f"per turn on the {Fore.MAGENTA}3x3 grid.{Fore.WHITE} The {Fore.GREEN}WINNER {Fore.WHITE}is")
    print(f"who {Fore.GREEN}succeeds {Fore.WHITE}in placing three of their")
    print(f"marks in a:")
    print(f"{Fore.GREEN}* {Fore.MAGENTA}Horizontal row")
    print(f"{Fore.GREEN}* {Fore.MAGENTA}Vertical row")
    print(f"{Fore.GREEN}* {Fore.MAGENTA}Diagonal row")
    print(SEPARATOR)
    print(f"{Fore.BLUE}Let's start the game!")
    print(SEPARATOR)

# Display the game board
def display_board(board):
    print(f"{Fore.MAGENTA}+---+---+---+")
    for i in range(0, 9, 3):
        print(
            f"{Fore.MAGENTA}| {colorize_mark(board[i])} "
            f"{Fore.MAGENTA}| {colorize_mark(board[i+1])} "
            f"{Fore.MAGENTA}| {colorize_mark(board[i+2])} {Fore.MAGENTA}|"
        )
        print(f"{Fore.MAGENTA}+---+---+---+")

def colorize_mark(mark):
    if mark == PLAYER_X:
        return f"{Fore.RED}{mark}"
    elif mark == PLAYER_O:
        return f"{Fore.BLUE}{mark}"
    return mark

# Check if a move is valid
def is_valid_move(board, move):
    is_digit = move.isdigit()
    in_range = 1 <= int(move) <= 9 if is_digit else False
    is_empty = board[int(move) - 1] == EMPTY_CELL if in_range else False
    return is_digit and in_range and is_empty

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
    board = [EMPTY_CELL] * 9
    current_player = PLAYER_X

    while True:
        display_board(board)
        print(SEPARATOR)
        move = input(f"Player {Fore.GREEN}{current_player}{Fore.WHITE}, please enter your move {Fore.GREEN}(1-9): ")
        print(SEPARATOR)
        if not is_valid_move(board, move):
            print(f"{Fore.RED}Invalid move. Please try again.")
            continue

        place_move(board, move, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print(f"{Fore.GREEN}Congratulations! Player {colorize_mark(current_player)} wins!")
            break

        if check_draw(board):
            display_board(board)
            print(f"{Fore.MAGENTA}It's a draw!")
            break

        # Switch player
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

# Run the game
if __name__ == "__main__":
    play_game()
