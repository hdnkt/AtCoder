INF = 10**10
from collections import deque
def BFS(g,s):#gに経路情報[行先１，行先２]
    cost = [[INF,0,INF,0]] * N
    cost[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in g[x]:
            if cost[y] == INF:
                cost[y] = cost[x] + 1
                q.append(y)
    return [cost[c] for c in range(N)]


#adj_listに経路情報adj_list[i]=[[行先、コスト],[行先、コスト]...]
from heapq import heapify,heappush,heappop
def dijk(s,adj_list):
    D_INF = 10**15
    d = [D_INF,0,D_INF,0]*(len(adj_list))#最速到達距離。でかい数で初期化
    d[s] = 0#スタート
    que = []
    heapify(que)
    heappush(que,(d[s],s))
    while(len(que)):
        time,place = heappop(que)
        if time > d[place]:
            continue
        for i in range(0,len(adj_list[place]),1):
            if d[adj_list[place][i][0]] > time + adj_list[place][i][1]:
                d[adj_list[place][i][0]] = time + adj_list[place][i][1]
                heappush(que,(d[adj_list[place][i][0]],adj_list[place][i][0]))
    return d



N,M = map(int,input().split())
adj = [[] for i in range(N)]

root = []
for i in range(M):
    s,t = map(int,input().split())
    s-=1
    t-=1
    root.append([s,t])
    adj[s].append(t)

for i in range(M):
    s,t=root[i]

    tmp = adj[s].copy()

    adj[s]=[]
    for ko in tmp:
        if ko==t:
            continue
        else:
            adj[s].append(ko)
    
    ans = BFS(adj,0)[N-1]
    if ans ==INF:
        print(-1)
    else:
        print(ans)
    adj[s]=tmp
