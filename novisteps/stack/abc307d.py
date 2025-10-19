#https://atcoder.jp/contests/abc307/tasks/abc307_d
'''
問題文
英小文字および (, ) からなる長さ 
N の文字列 
S が与えられます。
以下の操作を可能な限り繰り返したあとの 
S を出力してください。

S の連続部分文字列であって、最初の文字が ( かつ 最後の文字が ) かつ 最初と最後以外に ( も ) も含まないものを自由に 
1 つ選び削除する
なお、操作を可能な限り繰り返したあとの 
S は操作の手順によらず一意に定まることが証明できます。

制約
1≤N≤2×10^5
N は整数である
S は英小文字および (, ) からなる長さ N の文字列である
'''

n=int(input())
s=input()
b_c=0
stack=[]
for i in range(n):
    if s[i]=='(':
        b_c+=1
        stack.append(s[i])
    elif s[i]==')' and b_c>0:
        while True:
            a=stack.pop()
            if a=='(':
                b_c-=1
                break
    else:
        stack.append(s[i])
print(''.join(stack))
