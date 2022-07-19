#adj_listに経路情報adj_list[i]=[[行先、コスト],[行先、コスト]...]

N,M = map(int,input().split())

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

