def f(words,i=0,memo=None):
    if i==len(words):
        return len(memo)
    if memo==None:
        memo=set()
    cur=words[i]
    for j in range(len(words)):
        if i==j:
            continue
        memo.add(cur+words[j])
    return f(words,i+1,memo)

n=int(input())
a=[input() for _ in range(n)]
print(f(a))