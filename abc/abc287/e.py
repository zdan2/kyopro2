from collections import defaultdict
def node():
    return defaultdict(node)

n = int(input())
trie = node()
a=[]
for i in range(n):
    s=list(input())
    a.append(s)
    cur=trie
    for e in s:
        cur=cur[e]
    cur['#']=(i,len(s))
for i,e in enumerate(a):
    now=trie
    c=0
    for k in range(1,len(e)):
        if cur in 