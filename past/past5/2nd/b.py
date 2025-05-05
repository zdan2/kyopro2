n=int(input())
s=input()
t=''
for i in range(n):
    r=s[i]
    t=t.replace(r,'')+r
print(t)