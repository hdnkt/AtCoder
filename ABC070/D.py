N = int(input())
adj_list = [[] for i in range(N+1)]
for i in range(N-1):
    a,b,c, = map(int,input().split())
    adj_list[a].append([b,c])
    adj_list[b].append([a,c])

Q,s = map(int,input().split())


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
        if d[adj_list[place][i][0]] > time + adj_list[place][i][1]:#とりあえず円で
            d[adj_list[place][i][0]] = time + adj_list[place][i][1]
            heappush(que,(d[adj_list[place][i][0]],adj_list[place][i][0]))


ans = []
for i in range(Q):
    x,y = map(int,input().split())
    ans.append(d[x]+d[y])

for i in range(len(ans)):
    print(ans[i])