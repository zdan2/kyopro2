from bisect import bisect_left, bisect_right, insort_left
import sys

n = int(sys.stdin.readline())
offset = 0
elements = []

for _ in range(n):
    q = list(map(int, sys.stdin.readline().split()))
    if q[0] == 1:
        # オフセットを考慮して値を追加
        insort_left(elements, -offset)
    elif q[0] == 2:
        # オフセットを更新
        offset += q[1]
    elif q[0] == 3:
        # 実際の閾値を計算
        threshold = q[1] - offset
        # 削除する要素の開始インデックスを取得
        idx = bisect_left(elements, -threshold)
        count = len(elements) - idx
        if count > 0:
            # 削除と出力
            print(count)
            elements = elements[:idx]
        else:
            print(0)
