s,a,b,x=map(int,input().split())
print((x//(a+b)*a+min(x%(a+b),a))*s)