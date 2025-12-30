n=int(input())
a=list(map(int,input().split()))
stack=[]
for e in a:
    if stack and e==stack[-1][0]:
        stack[-1]=(e,stack[-1][1]+1)
    else:
        stack.append((e,1))
    if stack[-1][1]==4:
        stack.pop()
r=0
for _,v in stack:
    r+=v
print(r)