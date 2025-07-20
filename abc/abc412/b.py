s=input()
t=set(list(input()))
k=[]
for i in range(1,len(s)):
    if 'A'<=s[i]<='Z':
        k.append(s[i-1])
print('Yes' if all(e in t for e in k) else 'No')