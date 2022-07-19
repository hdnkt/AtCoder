from collections import defaultdict, namedtuple,deque
INF = 10**10

#adj_listに経路情報adj_list[i]=[[行先、コスト],[行先、コスト]...]

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

N,M = map(int,input().split())
adj = [[] for i in range(N)]

for i in range(M):
    a,b=map(int,input().split())
    adj[b-1].append(a-1)
    adj[a-1].append(b-1)

kist = []
K = int(input())
C = list(map(int,input().split()))
for i in range(K):
    tmp= BFS(adj,C[i]-1)
    tmm=[]
    for j in range(K):
        tmm.append(tmp[C[j]-1])
    kist.append(tmm)
dp = [[INF]*K for i in range(1<<K)]
 
for i in range(K):
    dp[1<<i][i]=1
 
for S in range(1<<K):
    for i in range(K):
        if S & (1<<i)==0:
            continue
        for j in range(K):
            dp[S][i] = min(dp[S^(1<<i)][j]+kist[i][j],dp[S][i])
 
 
ans = min(dp[S])
print(ans if ans !=INF else -1)