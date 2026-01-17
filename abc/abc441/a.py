p,q=map(int,input().split())
x,y=map(int,input().split())
print('Yes' if p<=x<p+100 and q<=y<q+100 else 'No')