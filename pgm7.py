def draw(board):
    print("\nCurrent Board:")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def take_input(board, turn):
    while True:
        pos = input(turn + "'s turn (choose position 1-9): ")
        if pos.isdigit() and 1 <= int(pos) <= 9 and board[int(pos) - 1] == ' ':
            board[int(pos) - 1] = turn
            break
        else:
            print("Invalid input, try again.")

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
                      (0, 4, 8), (2, 4, 6)] # Diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    return None

board = [' '] * 9
turn = 'X'
for _ in range(9):
    draw(board)
    take_input(board, turn)
    if check_win(board):
        draw(board)
        print(turn + " wins!")
        break
    turn = 'O' if turn == 'X' else 'X'
else:
    draw(board)
    print("It's a draw!")
