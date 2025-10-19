s = input()
n = len(s)
for i in range(n - 2):
    if s[i] == s[i+1]:
        print(i + 1, i + 2)
        exit()
    if s[i] == s[i+2]:
        print(i + 1, i + 3)
        exit()
if n >= 2 and s[n-2] == s[n-1]:
    print(n - 1, n)
    exit()
print(-1, -1)