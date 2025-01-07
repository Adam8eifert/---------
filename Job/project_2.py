"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Adam Seifert
email: seifert.promotion@gmail.com
"""


def print_intro():
    """Vypíše úvodní text a pravidla hry."""
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (X or O)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("the player who succeeds in placing three")
    print("of their marks in a:")
    print("* horizontal,")
    print("* vertical, or")
    print("* diagonal row")
    print("=" * 40)


def create_board():
    """Vytvoří prázdnou hrací plochu."""
    return [" " for _ in range(9)]


def print_board(board):
    """Zobrazí aktuální stav hrací plochy."""
    print("+---+---+---+")
    for row in range(3):
        print(f"| {board[row * 3]} | {board[row * 3 + 1]} | {board[row * 3 + 2]} |")
        print("+---+---+---+")


def is_valid_move(board, position):
    """Ověří, zda je tah validní (pole není obsazené a je v rozsahu 1-9)."""
    return position in range(1, 10) and board[position - 1] == " "


def make_move(board, position, player):
    """Umístí symbol hráče na zvolenou pozici."""
    board[position - 1] = player


def check_winner(board, player):
    """Zkontroluje, zda hráč vyhrál."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontální
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertikální
        [0, 4, 8], [2, 4, 6]              # diagonální
    ]
    return any(all(board[pos] == player for pos in combo) for combo in winning_combinations)


def is_draw(board):
    """Ověří, zda je remíza (všechna pole obsazená a žádný vítěz)."""
    return " " not in board


def get_player_input(board, player):
    """Požádá hráče o vstup a vrátí validní pozici."""
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (1-9): "))
            if is_valid_move(board, position):
                return position
            else:
                print("Invalid move. The position is either occupied or out of range.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def main():
    """Hlavní funkce hry."""
    print_intro()
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)
        position = get_player_input(board, current_player)
        make_move(board, position, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
