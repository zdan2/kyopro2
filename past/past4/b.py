x,y=map(int,input().split())
if y==0:
    print('ERROR')
    exit()
x*=100
a=int(x/y)
print(format(a/100,'.2f'))

