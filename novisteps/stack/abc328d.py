#https://atcoder.jp/contests/abc328/tasks/abc328_d
'''
問題文
A , B , C の 
3 種類の文字のみからなる文字列 
S が与えられます。

S が連続な部分文字列として文字列 ABC を含む限り、下記の操作を繰り返します。

S に連続な部分文字列として含まれる文字列 ABC のうち、
S の中で最も左にあるものを、
S から削除する。

上記の手順を行った後の、最終的な 
S を出力してください。

制約
S は A , B , C のみからなる長さ 
1 以上 2×10^5
  以下の文字列
'''
s=input()
stack=[]
i=0
while i<len(s):
    stack.append(s[i])
    i+=1
    if len(stack)<3:
        continue
    if stack[-3]=='A' and stack[-2]=='B' and stack[-1]=='C':
        stack.pop()
        stack.pop()
        stack.pop()
print(''.join(stack))



