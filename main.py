import random

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    # Add a 1 in 10 chance to make a random move (error)
    if random.randint(1, 10) == 1:
        return random.choice(get_empty_cells(board))

    best_score = -float('inf')
    move = None
    for i, j in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("🎮 Player (X) vs Computer (O) [1 in 10 chance computer makes mistake]")
    print_board(board)

    while True:
        # Player Move
        while True:
            try:
                row = int(input("Your move - Enter row (0-2): "))
                col = int(input("Your move - Enter col (0-2): "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Invalid or taken spot. Try again.")
            except ValueError:
                print("Please enter numbers from 0 to 2.")

        print_board(board)

        if check_win(board, "X"):
            print("🎉 You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # Computer Move
        print("🤖 Computer is thinking...")
        i, j = best_move(board)
        board[i][j] = "O"

        print_board(board)

        if check_win(board, "O"):
            print("💻 Computer wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

tic_tac_toe()
