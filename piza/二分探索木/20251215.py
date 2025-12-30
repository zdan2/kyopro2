class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
    
    def add(self,node):
        if not self.root:
            self.root=Node(node)
            return
        
        cur=self.root
        while True:
            if cur.val<node:
                if cur.right:
                    cur=cur.right
                else:
                    cur.right=Node(node)
                    break
            else:
                if cur.left:
                    cur=cur.left
                else:
                    cur.left=Node(node)
                    break
    
    def delete(self,num):
        pre=None
        cur=self.root
        while True:
            if cur.val==num:
                pre=cur
                if cur.right:
                    cur=cur.right
                elif cur.left:
                    cur=cur.left
                change_root(pre,cur)
                break
            elif cur.val<num:
                pre=cur
                cur=cur.right
            else:
                pre=cur
                cur=cur.left
    
    def change_root(self,pre_node,cur_node):
        if pre_node==None:
            self.root=cur_node
        while cur_node:
            cur_node=cur_node.left
        cur_node.left=pre_node.left

tree=Tree()
for e in [4,2,5,3,1,6,7]:
    tree.add((e))

print(tree.root.right.val)
            
    
                         
            
        