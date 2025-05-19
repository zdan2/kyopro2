n=int(input())
a,b,c,d=map(int,input().split())
x=input()
x=x.replace('.','')
x=int(x)
sum=a+2*b+3*c+4*d
sum*=1000
print(max(0,(sum-x*n+(x-1001))//(x-1000)))