a,b=map(int,input().split())
print(['Nein','Nine'][a+b==9 or a-b==9 or a*b==9 or 9*b==a])