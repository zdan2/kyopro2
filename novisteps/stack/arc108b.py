#https://atcoder.jp/contests/arc108/tasks/arc108_b
'''
問題文
長さ 
N の英小文字のみからなる文字列 
s が与えられます。 すぬけ君は 
s から fox という部分文字列を 
1 つ選んで取り除き、その前後の部分を連結する、という操作を何度でも行うことができます。

すぬけ君が操作を何度か行ったあと、
s の長さは最小でいくつになりえますか？

制約
1≤N≤2×10^5
 
s は英小文字のみからなる長さ N の文字列
'''

n=int(input())
s=input()
stack=[]
for i in range(n):
    stack.append(s[i])
    if len(stack)<3:
        continue
    if stack[-3:]==['f','o','x']:
        stack.pop()
        stack.pop()
        stack.pop()
print(len(stack))