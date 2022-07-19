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

def DFS(g,s):#gに経路情報[行先１，行先２]
    cost = [INF] * N
    cost[s] = 0
    q = deque([s])
    while q:
        x = q.pop()
        for y in g[x]:
            if cost[y] == INF:
                cost[y] = cost[x] + 1
                q.append(y)
    return [cost[c] for c in range(N)]


N,M = map(int,input().split())
adj = [[] for i in range(N)]