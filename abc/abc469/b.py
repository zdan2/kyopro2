n=int(input())
s='x'+input()+'x'
print(sum(s[i-1]==s[i]==s[i+1]=='x' for i in range(1,n+1))) 