INF = 10**15

#adj_listに経路情報adj_list[i]=[[行先、コスト],[行先、コスト]...]

from heapq import heapify,heappush,heappop
def dijk(s,adj_list):
    D_INF = 10**15
    d = [D_INF]*(len(adj_list))#最速到達距離。でかい数で初期化
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

N,M,P = map(int,input().split())

adj_list=[[]for i in range(N+1)]
bel_list=[[]for i in range(N+1)]
ABC = [list(map(int,input().split())) for i in range(M)]

for i in range(M):
    A,B,C = ABC[i]
    adj_list[B].append([A,1])

d=dijk(N,adj_list)

#到着地がINFだったら辺貼らない
for i in range(M):
    A,B,C = ABC[i]
    if d[B] != INF:
        bel_list[A].append([B,P-C])

V = N+1
r = 1
G = bel_list

# V: グラフの頂点数
# r: 始点
# G[v] = [(w, cost), ...]: 頂点vからコストcostで到達できる頂点w
INF = 10**18
dist = [INF] * V
dist[r] = 0
update = 1
for _ in range(V):
    update = 0
    for v, e in enumerate(G):
        for t, cost in e:
            if dist[v] != INF and dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                update = 1
    if not update:
        break
else:
    # 負閉路検出処理
    print(-1)
    exit()

print(-dist[N] if dist[N]<0 else 0)
