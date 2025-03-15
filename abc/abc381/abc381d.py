n=int(input())
a=list(map(int,input().split()))

i=0
r=0
while True:
    if i+1>=n:
        break
    if a[i]==a[i+1]:
        j=i+2
        s=set()
        s.add(a[i])
        c=1
        while True:
            if j+1>=n:
                break
            if a[j]==a[j+1] and a[j] not in s:
                s.add(a[j])
                c+=1
                j+=2
            else:
                break
        r=max(r,c)
        i=j-2
    i+=1
print(r*2)
        