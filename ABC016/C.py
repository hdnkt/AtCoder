INF = 10**10
N,M = map(int,input().split())
from collections import defaultdict, namedtuple,deque

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

adj = [[]for i in range(N)]

for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    adj[a].append(b)
    adj[b].append(a)

cost = []
for i in range(N):
    cost.append(BFS(adj,i))

for i in range(N):
    tmp=0
    for j in range(N):
        if cost[i][j]==2:
            tmp+=1
    print(tmp)