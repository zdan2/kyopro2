class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.is_black=[False]*n
        self.black_count=[0]*n
    
    def merge(self,a,b):
        root_a=self.find(a)
        root_b=self.find(b)
        if root_a==root_b:
            return
        if root_b<root_a:
            root_a,root_b=root_b,root_a
        self.parent[root_b]=root_a
        self.black_count[root_a] += self.black_count[root_b]
    
    def find(self,a):
        if self.parent[a]==a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def bw(self, a):
        root_a = self.find(a)
        if self.is_black[a]:
            self.black_count[root_a] -= 1
            self.is_black[a] = False
        else:
            self.black_count[root_a] += 1
            self.is_black[a] = True
            
    def chk(self,a):
        root_a=self.find(a)
        if self.black_count[root_a]>0:
            return True
        return False

n,q=map(int,input().split())
dsu=DSU(n+1)
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        dsu.merge(x[1],x[2])
    if x[0]==2:
        dsu.bw(x[1])
    if x[0]==3:
        print('Yes' if dsu.chk(x[1]) else 'No')