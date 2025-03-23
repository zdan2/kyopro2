n, m = map(int, input().split())
c_list = list(map(int, input().split()))
s_list = list(map(int, input().split()))
d_list = list(map(int, input().split()))

# d(i)=1,2,3に対応するものを r[0], r[1], r[2] に振り分け
r = [[], [], []]
for i in range(n):
    r[d_list[i] - 1].append([c_list[i], s_list[i]])

# dp[x] = [xカロリー消費時の最大幸福度, 最後に使った食品の種類]
dp = [[-1, 0] for _ in range(m + 1)]

# 1種類目での遷移 (初期化)
for cal, happ in r[0]:
    if cal <= m:
        dp[cal] = max(dp[cal], [happ, 1], key=lambda x: x[0])

# 2種類目での遷移
for cal, happ in r[1]:
    # 逆順にループすることで同一アイテムの多重使用を防ぐ
    for used_cal in range(m - cal, -1, -1):
        if dp[used_cal][0] != -1:  # 何らかの方法で到達可能
            new_happ = dp[used_cal][0] + happ
            if dp[used_cal + cal][0] < new_happ:
                dp[used_cal + cal] = [new_happ, 2]

# 3種類目での遷移
for cal, happ in r[2]:
    # 同様に逆順にループ
    for used_cal in range(m - cal, -1, -1):
        # 最後に使った食品の種類が2の状態からのみ遷移
        if dp[used_cal][0] != -1 and dp[used_cal][1] == 2:
            new_happ = dp[used_cal][0] + happ
            if dp[used_cal + cal][0] < new_happ:
                dp[used_cal + cal] = [new_happ, 3]

# dp の中で「最後に使った食品の種類 == 3」のものから最大幸福度を探索
max_happiness = -1
for happiness, kind in dp:
    if kind == 3:
        max_happiness = max(max_happiness, happiness)
print(max_happiness )
