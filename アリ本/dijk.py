#使い方
#adj_list[]に[つながる先,コスト]のリストをいれてグラフを表現
#sがスタート地点
#N+1になってるのはどうせ出題は1-indexdだから
#N：頂点数　M:辺数　s：スタート地点　dに答え（sからの最短経路）が格納される
adj_list = [[] for i in range(N+1)]
for i in range(M):
    a,b,c, = map(int,input().split())
    adj_list[a].append([b,c])
    adj_list[b].append([a,c])

from heapq import heapify,heappush,heappop
D_INF = 10**15
d = [D_INF]*(N+1)#最速到達距離。でかい数で初期化
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