n = int(input())
s = input()
mod = 10**9 + 7

total_sum = 0
f = 1
for i in range(n-1, -1, -1):
    digit = int(s[i])
    total_sum = (total_sum + digit * f * (i + 1)) % mod
    f = (f * 10 + 1) % mod

print(total_sum)
