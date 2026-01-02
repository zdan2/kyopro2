t=int(input())
for _ in range(t):
    s=input()
    a=int(s)
    b=int(input())
    for i in range(len(s)):
        if a==b:
            print(i)
            break
        a=a%(10**(len(s)-1))
        a*=10
        a+=int(s[i])
    else:
        print(-1)