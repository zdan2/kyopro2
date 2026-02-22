n=int(input())
bit=[0]*(n+1)

def add(i,x):
    i+=1
    while i<=n:
        bit[i]+=x
        i+=i&-i

def 