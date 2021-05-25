#教訓　python再帰がちんちんくらい遅い

from collections import deque 
#スタック
s = deque([])

N,Q = map(int,input().split())
node = [[]for i in range(0,N+1,1)]
for i in range(0,N-1,1):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)
node_score = [0]*(N+1)#スコア
for i in range(0,Q,1):
    p,x = map(int,input().split())
    node_score[p] += x

ans = [0]*(N+1)

s.append([1,0])
while len(s) > 0:
    n,preN = s.pop()
    ans[n] = ans[preN]+node_score[n]
    for to in node[n]:
        if to != preN:
            s.append([to,n])

print(" ".join(list(map(str,ans[1:N+1]))))
        

