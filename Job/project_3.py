"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Adam Seifert
email: seifert.promotion@gmail.com
"""

# Import libraries
from colorama import Fore, init  
from typing import List, Tuple

# Initialize colorama 
init(autoreset=True)

# Constants 
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_CELL = " "
SEPARATOR = f"{Fore.CYAN}{'=' * 40}"

def display_welcome() -> None:
    """Display welcome message and game rules."""
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

def is_valid_move(board: List[List[str]], move: Tuple[int, int]) -> bool:
    """Check if the move is valid."""
    row, col = move
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == EMPTY_CELL

def get_move() -> Tuple[int, int]:
    """Prompt the player to enter a move and return it as a tuple of integers."""
    while True:
        try:
            move = input("Enter your move (row and column): ").split()
            if len(move) != 2:
                raise ValueError("Please enter two numbers.")
            row, col = int(move[0]), int(move[1])
            return row, col
        except ValueError as e:
            print(f"{Fore.RED}Invalid input: {e}. Please try again.")

def place_move(board: List[List[str]], move: Tuple[int, int], player: str) -> None:
    """Place the player's move on the board."""
    row, col = move
    board[row][col] = player

def check_winner(board: List[List[str]], player: str) -> bool:
    """Check if the player has won."""
    # Check rows, columns, and diagonals
    return any(
        all(cell == player for cell in row) for row in board
    ) or any(
        all(row[i] == player for row in board) for i in range(3)
    ) or all(
        board[i][i] == player for i in range(3)
    ) or all(
        board[i][2 - i] == player for i in range(3)
    )

def check_draw(board: List[List[str]]) -> bool:
    """Check if the game is a draw."""
    return all(cell != EMPTY_CELL for row in board for cell in row)

def display_board(board: List[List[str]]) -> None:
    """Display the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def play_game() -> None:
    """Main function to play the game."""
    board = [[EMPTY_CELL] * 3 for _ in range(3)]
    current_player = PLAYER_X

    display_welcome()

    while True:
        display_board(board)
        move = get_move()

        if not is_valid_move(board, move):
            print(f"{Fore.RED}Invalid move. Try again.")
            continue

        place_move(board, move, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print(f"{Fore.GREEN}Congratulations! Player {current_player} wins!")
            break

        if check_draw(board):
            display_board(board)
            print(f"{Fore.GREEN}It's a draw!")
            break

        # Switch player
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    play_game()