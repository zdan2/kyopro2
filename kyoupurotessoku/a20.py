s=list(input())
t=list(input())

if len(s)>=len(t):
    a=s
    b=t
else:
    a=t
    b=s
    
n=len(a)
dp=a.copy()