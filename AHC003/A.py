from sys import stdin
input = stdin.readline

import time
start = time.time()

#adj_listに経路情報adj_list[i]=[[行先、コスト],[行先、コスト]...]
from heapq import heapify,heappush,heappop
def dijk(s,adj_list):
    D_INF = 10**15
    d = [D_INF]*(len(adj_list))#最速到達距離。でかい数で初期化
    pre = [-1 for i in range(30*30)]
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
                pre[adj_list[place][i][0]]=place
                heappush(que,(d[adj_list[place][i][0]],adj_list[place][i][0]))
    return d,pre

#ifでかけ
def ippo(sx,sy,tx,ty):
    for j in range(tx-sx):
        return "D"
    for j in range(sx-tx):
        return "U"
    for j in range(ty-sy):
        return "R"
    for j in range(sy-ty):
        return "L"


rireki = {}

adj_list = [[] for i in range(30*30)]
for i in range(30):
    for j in range(30):
        for vec in [[1,0],[-1,0],[0,1],[0,-1]]:
            I = i+vec[0]
            J = j+vec[1]
            if 0<=I and I<30 and 0<=J and J<30:
                adj_list[30*i+j].append([30*I+J,1])
            s,t = 30*i+j,30*I+J
            if s < t:
                rireki[tuple([s,t])]=[1]

for i in range(1000):
    Sx,Sy,Tx,Ty = map(int,input().split())
    #最短経路
    cost,pre=dijk(30*Sx+Sy,adj_list)

    #経路復元
    tmp = Tx*30+Ty
    path = [[tmp//30,tmp%30]]
    while tmp!=Sx*30+Sy:
        tmp = pre[tmp]
        path.append([tmp//30,tmp%30])

    path.reverse()
    ans = []
    for i in range(len(path)-1):
        sx,sy=path[i]
        tx,ty=path[i+1]
        ans.append(ippo(sx,sy,tx,ty))

    print("".join(ans),flush=True)
    score = int(input())
    #score = 5
    #重み更新
    per = score/(len(path)-1)
    adj_list = [[] for i in range(30*30)]
    for i in range(len(path)-1):
        s = path[i][0]*30+path[i][1]
        t = path[i+1][0]*30+path[i+1][1]
        if s>t:
            s,t=t,s
        rireki[tuple([s,t])].append(per)
    for i in range(30):
        for j in range(30):
            for vec in [[1,0],[-1,0],[0,1],[0,-1]]:
                I = i+vec[0]
                J = j+vec[1]
                if 0<=I and I<30 and 0<=J and J<30:
                    s,t =  s,t = 30*i+j,30*I+J
                    if s > t:
                        s,t = t,s
                    tmpcost = sum(rireki[tuple([s,t])])//len(rireki[tuple([s,t])])
                    adj_list[30*i+j].append([30*I+J,tmpcost])

                