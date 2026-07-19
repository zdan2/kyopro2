r=[]
s=input()
l=len(s)-1
for i,e in enumerate(s):
    if e=='C':
        r.append(i)
print(sum((min(e,l-e))+1 for e in r))