import heapq

N = int(input())
A = list(map(int, input().split()))

# ステップ1: 各宇宙人が受け取った石の数を計算する
stones_received = [0] * N
# (有効期限が切れる年) を管理する最小ヒープ
expirations_pq = []
# 現在、お祝いを渡せる成人の数
givers = 0

# 1年後からN年後までシミュレーション
for year in range(1, N + 1):
    # --- 今年の始めに有効期限が切れる成人を処理 ---
    while expirations_pq and expirations_pq[0] == year:
        heapq.heappop(expirations_pq)
        givers -= 1
        
    # --- 新成人の処理 ---
    # 新しく成人する宇宙人のインデックス (0-indexed)
    new_adult_idx = year - 1
    
    # この時点でのお祝いをくれる人数が、受け取る石の数
    stones_received[new_adult_idx] = givers
    
    # 新成人がお祝いを渡せる側に追加される
    total_stones = A[new_adult_idx] + stones_received[new_adult_idx]
    
    if total_stones > 0:
        givers += 1
        # この新成人の有効期限（石が0になる年）を計算してヒープに追加
        # year年に成人し、total_stones個の石を持つ。来年から1個ずつ渡す。
        # total_stones回渡せるので、year + total_stones年まで持つ。
        # 有効期限が切れるのは year + total_stones 年の終わり、つまり次の year + total_stones + 1 年の始め。
        expiration_year = year + total_stones + 1
        heapq.heappush(expirations_pq, expiration_year)

# ステップ2: 最終的な石の数を計算する
final_stones = [0] * N
for i in range(N):
    # 宇宙人iが成人してからN年後までの、お祝いを渡す機会の回数
    opportunities_to_give = N - (i + 1)
    
    # 宇宙人iが使える石の総数
    total_available_stones = A[i] + stones_received[i]
    
    # 実際に渡した石の数
    stones_given = min(opportunities_to_give, total_available_stones)
    
    # 最終的な石の数
    final_stones[i] = total_available_stones - stones_given

print(*final_stones)