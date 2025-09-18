i,j=map(int,input().split('-'))
if j%8==0:
    i+=1
print(f'{i}-{j%8+1}')