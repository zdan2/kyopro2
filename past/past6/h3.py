import heapq

# 入力の取得
n, m, k, q = map(int, input().split())

# 缶詰を分類
hq0 = []  # 缶切り不要の缶詰
hq1 = []  # 缶切り必要の缶詰

for _ in range(n):
    p, t = map(int, input().split())
    if t == 0:
        heapq.heappush(hq0, p)  # 価格順に並ぶ
    else:
        heapq.heappush(hq1, p)

# 最小コスト計算
cost = 0
kc = k  # 現在の缶切りの残り使用可能数
selected = 0  # 選択済み缶詰の数

while selected < m:
    # 缶切り不要缶詰の最安値
    if hq0:
        can0 = heapq.heappop(hq0)
    else:
        can0 = float('inf')  # 無限大（選択肢がない場合）

    # 缶切り必要缶詰の最安値
    if hq1:
        can1 = heapq.heappop(hq1)
    else:
        can1 = float('inf')  # 無限大（選択肢がない場合）

    # 缶切りが不要な缶詰を選ぶ場合
    if can0 <= can1 + (q if kc == 0 else 0):
        cost += can0
        selected += 1
    else:
        # 缶切りが必要な缶詰を選ぶ場合
        if kc == 0:  # 缶切りを購入
            cost += q
            kc = k  # 缶切りの使用回数をリセット

        cost += can1
        kc -= 1  # 缶切りを1つ使用
        selected += 1

    # 使用しなかった缶詰はヒープに戻す
    if can0 < float('inf') and can0 != cost:
        heapq.heappush(hq0, can0)
    if can1 < float('inf') and can1 != cost:
        heapq.heappush(hq1, can1)

print(cost)
