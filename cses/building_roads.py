from collections import defaultdict
class UF:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
    
    def find(self,a):
        if self.parent[a]==a:
            return a
        return self.find(self.parent[a])
    
    def merge(self,a,b):
        root_a=self.find(a)
        root_b=self.find(b)
        if root_a==root_b:
            return
        if self.size[a]>=self.size[b]:
            self.parent[b]=root_a
            self.size[a]+=self.size[b]
        else:
            self.parent[a]=root_b
            self.size[b]+=self.size[a]
    
    def groups(self):
        dict=defaultdict(list)
        for i in range(1,len(self.parent)):
            p=self.parent[i]
            dict[p].append(i)
        return dict
            
n,m=map(int,input().split())
uf=UF(n)
for _ in range(m):
    a,b=map(int,input().split())
    uf.merge(a,b)
r=[k for k,v in uf.groups().items()]
print(len(r)-1)
for i in range(1,len(r)):
    print(r[0],r[i])