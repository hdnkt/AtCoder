INF = 10**10
from collections import deque
def BFS(g,s):#gに経路情報[行先１，行先２]
    cost = [INF] * N
    cost[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in g[x]:
            if cost[y] == INF:
                cost[y] = cost[x] + 1
                q.append(y)
    return [cost[c] for c in range(N)]

#いつものように経路情報を渡すと
#子の数（自分含む）を教えてくれる
def KIDS(adj,s):
    cost = BFS(adj,s)
    deeper = [[cost[i],i] for i in range(N)]
    deeper.sort(reverse=True)
    kids = [1 for i in range(N)]
    for k in range(N):
        i = deeper[k][1]
        for pair in adj[i]:
            if cost[pair]<cost[i]:
                kids[pair]+=kids[i]
    return kids

N = int(input())
u = [list(map(int,input().split())) for i in range(N-1)]

adj = [[] for i in range(N)]
for i in range(N-1):
    a,b = u[i]
    a-=1
    b-=1
    u[i]=[a,b]
    adj[a].append(b)
    adj[b].append(a)

kids=KIDS(adj,0)

ans = 0
for i in range(N-1):
    a,b = u[i]
    tmp = min(kids[a],kids[b])
    ans+=tmp*(N-tmp)

print(ans)