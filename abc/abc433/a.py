x,y,z=map(int,input().split())
for i in range(z*max(x,y)+1):
    if x%y==0 and x//y==z:
        print('Yes')
        exit()
    x+=1
    y+=1
print('No')