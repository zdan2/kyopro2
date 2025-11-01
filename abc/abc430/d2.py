from collections import defaultdict
from sortedcontainers import SortedList

n = int(input())
x = list(map(int, input().split()))

r = SortedList([0])      # 既存点のソート済み集合
d = defaultdict(list)    # 各点 -> [左距離, 右距離]
d[0] = [0, 0]
c = 0                    # 距離合計（各点の左右距離の総和）

for e in x:
    idx = r.bisect(e)

    if 0 < idx < len(r):
        # 中央に挿入： r[idx-1] ... e ... r[idx]
        L = r[idx - 1]
        R = r[idx]

        # 既存の左右隣の「元の距離」
        o_l = d[L][1]   # L の右距離（= R-L のはず）
        o_r = d[R][0]   # R の左距離（= R-L のはず）

        # 新しく割れる距離
        d_l = e - L
        d_r = R - e

        # コスト更新（新規点ぶん 2*(d_l+d_r) を足し、隣の古い分 o_l+o_r を引く）
        c-=(o_l+o_r)
        c+=2*d_l+d_r

        # 隣接情報更新
        d[L][1] = d_l
        d[R][0] = d_r
        d[e] = [d_l, d_r]

    else:  # idx == len(r) 末尾に挿入
        L = r[-1]
        dist = e - L

        # 末尾側は「新規点の左距離 + 既存末尾の右距離(0→dist)」で 2*dist 増える
        c += 2 * dist

        d[L][1] = dist
        d[e] = [dist, 0]

    r.add(e)

# 必要なら最終状態を出力
    print(c)
    print(d)
# print(dict(d))
