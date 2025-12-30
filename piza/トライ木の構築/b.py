trie = [{'a':''}]
n,m=map(int,input().split())
s = input()
cd=trie[0]
key='a'
for i,e in enumerate(s):
    if e not in cd:
        cd[key]=e
        key=e
    if len(trie)<i+2:
        trie.append({})
    cd=trie[i+1]
for _ in range(m):
    i,k=input().split()
    i=int(i)
    if k in trie[i]:
        print(trie[i][k]) 
    else:
        print('#')   
