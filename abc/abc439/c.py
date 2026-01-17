n=int(input())
sqrt=int(n**0.5)+1
s=set()
d=set()
for x in range(1,sqrt-1):
    ylim=int((n-x*x)**0.5)+1
    for y in range(x+1,ylim):
        c=x*x+y*y
        if c<=n and c not in s:
            s.add(c)
        elif c in s:
            d.add(c)
s^=d
print(len(s))
print(*sorted(s))