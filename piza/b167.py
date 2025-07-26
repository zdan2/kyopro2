N=int(input())
game_map=[list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        game_map[i][j]=int(game_map[i][j])

repaired_map = [row[:] for row in game_map]

CONNECTS = {
    1: [False, False, True,  True],  # 左右
    2: [True,  True,  False, False], # 上下
    3: [True,  False, False, True],  # 上右
    4: [True,  False, True,  False], # 上左
    5: [False, True,  False, True],  # 下右
    6: [False, True,  True,  False]  # 下左
}

# 地図のすべてのマスをチェック
for r in range(N):
    for c in range(N):
        # 壊れた壁(7)が見つかった場合
        if game_map[r][c] == 7:
            connects_up = False
            connects_down = False
            connects_left = False
            connects_right = False

            # 上のマスを確認 (r > 0)
            if r > 0 and game_map[r-1][c] in CONNECTS:
                # 上の壁が「下」に接続口を持っているか
                if CONNECTS[game_map[r-1][c]][1]:
                    connects_up = True

            # 下のマスを確認 (r < N-1)
            if r < N - 1 and game_map[r+1][c] in CONNECTS:
                # 下の壁が「上」に接続口を持っているか
                if CONNECTS[game_map[r+1][c]][0]:
                    connects_down = True

            # 左のマスを確認 (c > 0)
            if c > 0 and game_map[r][c-1] in CONNECTS:
                # 左の壁が「右」に接続口を持っているか
                if CONNECTS[game_map[r][c-1]][3]:
                    connects_left = True

            # 右のマスを確認 (c < N-1)
            if c < N - 1 and game_map[r][c+1] in CONNECTS:
                # 右の壁が「左」に接続口を持っているか
                if CONNECTS[game_map[r][c+1]][2]:
                    connects_right = True

            new_piece = 0
            if connects_up and connects_down:
                new_piece = 2
            elif connects_left and connects_right:
                new_piece = 1
            elif connects_up and connects_left:
                new_piece = 6
            elif connects_up and connects_right:
                new_piece = 3
            elif connects_down and connects_left:
                new_piece = 5
            elif connects_down and connects_right:
                new_piece = 4

            repaired_map[r][c] = new_piece
for row in repaired_map:
    print(''.join(str(r) for r in row))
