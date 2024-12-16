N = int(input("Enter the number of queens: "))
board = [[0] * N for _ in range(N)]

def is_safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(row):
    if row == N:
        return True
    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1
            if solve_n_queens(row + 1):
                return True
            board[row][col] = 0
    return False

if solve_n_queens(0):
    for row in board:
        print(row)
else:
    print("No solution exists")
