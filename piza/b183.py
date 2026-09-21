n, m = map(int, input().split())
order = list(map(int, input().split()))
board = [[-1] * n for _ in range(n)]
def is_winner(row, col, player):
    if all(board[row][j] == player for j in range(n)):
        return True
    if all(board[i][col] == player for i in range(n)):
        return True
    if row == col:
        if all(board[i][i] == player for i in range(n)):
            return True
    if row + col == n - 1:
        if all(board[i][n - 1 - i] == player for i in range(n)):
            return True
    return False
op=[list(map(int,input().split())) for _ in range(n*n)]
for turn in range(n*n):
    h, w = op[turn]
    row = h - 1
    col = w - 1
    player = order[turn % m]
    board[row][col] = player
    if is_winner(row, col, player):
        print(player, turn + 1)
        break
else:
    print(-1)