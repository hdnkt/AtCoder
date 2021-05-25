# cost[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
# cost
INF = 10**15
def washal(V,cost):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if cost[i][k]!=INF and cost[k][j]!=INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost


N,M = map(int,input().split())

cost = [[INF if i!=j else 0 for j in range(N)] for i in range(N)]


for i in range(M):
    a,b,t=map(int,input().split())
    a=a-1
    b=b-1
    cost[a][b]=t
    cost[b][a]=t

ans = washal(N,cost)

ret = INF
for i in range(N):
    ret = min(ret,max(ans[i]))
print(ret)