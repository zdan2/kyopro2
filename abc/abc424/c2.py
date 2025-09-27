class UF:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
    
    def merge(self,a,b):
        if self.parent[a]==self.parent[b]:
            return
        root_a=self.find(a)
        root_b=self.find(b)
        if root_a>root_b:
            root_a,root_b=root_b,root_a
            self.parent[b]=root_a

    def find(self,a):
        if self.parent[a]==a:
            return a
        return self.find(self.parent[a])
    
    def d(self):
        print(self.parent)
               

n=int(input())
uf=UF(n+1)
for i in range(1,n+1):
    
