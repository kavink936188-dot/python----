import random

board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True

    return False


def is_board_full():
    return " " not in board


def bot_move():
    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    if empty_positions:
        move = random.choice(empty_positions)
        board[move] = "O"
        print(f"Bot chose position {move + 1}")


def play_game():
    print("TIC TAC TOE")
    print("You = X")
    print("Bot = O")

    while True:
       
        print_board()

        try:
            move = int(input("You, choose a position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position! Choose a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("That position is already taken!")
                continue

            board[move] = "X"

           
            if check_winner("X"):
                print_board()
                print("You win!")
                break

           
            if is_board_full():
                print_board()
                print("It's a draw!")
                break

            
            bot_move()

           
            if check_winner("O"):
                print_board()
                print("Bot wins!")
                break

            
            if is_board_full():
                print_board()
                print("It's a draw!")
                break

        except ValueError:
            print("Please enter a valid number.")


play_game()