from collections import defaultdict
n = int(input())
st = [tuple(input().split()) for _ in range(n)]
freq = defaultdict(int)
for s, t in st:
    for name in {s, t}: 
        freq[name] += 1
for s, t in st:
    if freq[s] > 1 and freq[t] > 1:
        print("No")
        break
else:
    print("Yes")   