n,a,b,c=map(int,input().split())
bar=[int(input()) for _ in range(n)]
t=[a,b,c]
def f(arr=None,i=0):
    if arr is None:
        arr=[[],[],[]]
    if i==n:
        r=0
        for i in range(3):
            c=0
            if not arr[i]:
                return float('inf')
            c+=(len(arr[i])-1)*10
            c+=abs(sum(arr[i])-t[i])
            r+=c
        return r

    c1=f([arr[0]+[bar[i]],arr[1],arr[2]],i+1)
    c2=f([arr[0],arr[1]+[bar[i]],arr[2]],i+1)
    c3=f([arr[0],arr[1],arr[2]+[bar[i]]],i+1)
    c4=f([arr[0],arr[1],arr[2]],i+1)
    
    return min(c1,c2,c3,c4)

print(f())