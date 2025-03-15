n, k = map(int, input().split())
s = list(input())
a = []
h = 0

for i in range(n):
    if s[i] == '1' and h == 0:
        l = i 
        h = 1
    if s[i] == '0' and h == 1:
        r = i - 1 
        a.append((l, r))
        h = 0
if h == 1:
    r = n - 1
    a.append((l, r))

t = s.copy()

r_prev = a[k - 2][1]  
l_k = a[k - 1][0]  
r_k = a[k - 1][1]  
length_k = r_k - l_k + 1  

for i in range(r_prev + 1, r_prev + length_k + 1):
    t[i] = '1'
for i in range(r_prev + length_k + 1, r_k + 1):
    t[i] = '0'

print(''.join(t))
