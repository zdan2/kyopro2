N = int(input())

TABLE = {
    1 | 2: 1,  # 3: 左(1) + 右(2) -> 部品1
    4 | 8: 2,  # 12: 上(4) + 下(8) -> 部品2
    4 | 2: 3,  # 6: 上(4) + 右(2) -> 部品3
    4 | 1: 4,  # 5: 上(4) + 左(1) -> 部品4
    8 | 2: 5,  # 10: 下(8) + 右(2) -> 部品5
    8 | 1: 6   # 9: 下(8) + 左(1) -> 部品6
}

input_data = [list(input()) for _ in range(N)]
A = [[int(char) for char in row] for row in input_data]

for r in range(N):
    for c in range(N):
        # 壊れた壁(7)でなければ次へ
        if A[r][c] != 7:
            continue

        # 接続方向を記録するビットマスク
        mask = 0

        # 上のマスを確認
        if r > 0 and A[r-1][c] in [2, 5, 6]:  # 上のマスにある部品が「下向き」に接続口を持つか
            mask |= 4  # 「上」方向への接続が確定

        # 下のマスを確認
        if r < N - 1 and A[r+1][c] in [2, 3, 4]:  # 下のマスにある部品が「上向き」に接続口を持つか
            mask |= 8  # 「下」方向への接続が確定

        # 左のマスを確認
        if c > 0 and A[r][c-1] in [1, 3, 5]:  # 左のマスにある部品が「右向き」に接続口を持つか
            mask |= 1  # 「左」方向への接続が確定

        # 右のマスを確認
        if c < N - 1 and A[r][c+1] in [1, 4, 6]:  # 右のマスにある部品が「左向き」に接続口を持つか
            mask |= 2  # 「右」方向への接続が確定
        
        # 確定した接続方向(mask)に応じて、テーブルから正しい部品番号を取得
        A[r][c] = TABLE[mask]

for row in A:
    print(''.join(str(x) for x in row))