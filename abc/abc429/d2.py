from collections import Counter
import sys

# 入力を受け取る
n, m, cc = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# --- 周期性の処理 ---
# ro: 何周分か (cc // n)
# rem: 残りの個数 (cc % n)
ro = cc // n
rem = cc % n

# ro周分のコスト(区間幅)を先に加算する
# 1周分のコストは、円周の長さ m
res = ro * m

# もしrem=0 (nの倍数個) なら、追加で探す必要はない
if rem == 0:
    print(res)
    # プログラムを終了
    sys.exit()

# --- rem個の点を集める最小区間幅を探す ---

# aの各値の出現回数をカウントし、値でソート
# c = [(値1, 個数1), (値2, 個数2), ...]
c = sorted(Counter(a).most_common())
l_unique = len(c)

# 円周上であることを考慮し、リストを2倍に拡張する
# (値 + m, 個数) を追加
c += [(c[i][0] + m, c[i][1]) for i in range(l_unique)]

# 個数の累積和 (Cumulative Sum) 配列 ca を作成
# ca = [(値1, 累積個数1), (値2, 累積個数2), ...]
# 計算を簡単にするため、ダミーの先頭要素 (値, 0) を追加する
ca = [(c[0][0] - 1, 0)] 
for val, count in c:
    ca.append((val, ca[-1][1] + count))

# --- スライディングウィンドウ (尺取り法) ---
min_rem_range = float('inf')  # rem個を集めるための最小区間幅
l = 1  # ウィンドウの左端 (ca のインデックス)

# r (ウィンドウの右端) を 1 から順に動かす
for r in range(1, len(ca)):
    # ウィンドウ内の個数 (lからrまで) を計算
    # ca[r][1] = (0からrまでの合計)
    # ca[l-1][1] = (0からl-1までの合計)
    # 差分 = (lからrまでの合計)
    count_in_window = ca[r][1] - ca[l-1][1]

    # ウィンドウ内の個数が rem 以上になるまで
    while count_in_window >= rem:
        # このときの区間幅を計算
        # 区間幅 = (右端の値) - (左端の値)
        current_range = ca[r][0] - ca[l][0]
        
        # 最小値を更新
        min_rem_range = min(min_rem_range, current_range)
        
        # ウィンドウを左から縮める (l を進める)
        l += 1
        
        # (l > r になることはないが、念のため)
        if l > r:
            break
            
        # 縮めた後のウィンドウの個数を再計算
        count_in_window = ca[r][1] - ca[l-1][1]

# 最初に計算した ro周分のコスト + rem個分の最小コスト
print(res + min_rem_range)

# 入出力を高速化 (AtCoderなどでは input() よりこちらが推奨されます)
# import sys
# n,m,cc=map(int,sys.stdin.readline().split())
# a=list(map(int,sys.stdin.readline().split()))