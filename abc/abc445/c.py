n = int(input())
a = list(map(int, input().split()))
nxt = [x - 1 for x in a]
ans = [0] * n
for i in range(n - 1, -1, -1):
    if nxt[i] == i:
        ans[i] = i + 1
    else:
        ans[i] = ans[nxt[i]]
print(*ans)
