import heapq

n = int(input())
s = set()
takahasi = 0
aoki = 0
ta = []
ao = []

for i in range(1, n + 1):
    a, b = map(int, input().split())
    # heapqは最小ヒープなので、最大ヒープとして使うために負の値を使用
    heapq.heappush(ta, (-a, -(a - b), i))  # 2つ目の値も負にして降順にソート
    heapq.heappush(ao, (-b, -(b - a), i))  # こちらも同様

for _ in range(n):
    while ta:
        x, _, idx = heapq.heappop(ta)
        if idx not in s:
            takahasi += -x  # 負の値を正に戻す
            s.add(idx)
            break
    while ao:
        x, _, idx = heapq.heappop(ao)
        if idx not in s:
            aoki += -x  # 負の値を正に戻す
            s.add(idx)
            break

print(takahasi - aoki)
