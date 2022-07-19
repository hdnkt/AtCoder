
N = int(input())
ab = [list(map(int,input().split())) for i in range(N-1)]#木でしょどうせ
#1-indexです
adj = [[]for i in range(N+1)]
for i in range(N-1):
    a,b = ab[i]
    adj[a].append(b)
    adj[b].append(a)


from collections import deque 
#スタック
s = deque([])

cost = [10**10]*(N+1)

#1スタート故に1,0
s.append([1,0])
while len(s)>0:
    place,time = s.pop()
    if time > cost[place]:
        continue
    cost[place]=time
    for i in adj[place]:
        if time < cost[i]:
            s.append([i,time+1])


#ここまで普通のbfs(cost[i]には1からの最短経路が格納)
root = [N]
nowp = N
nowt = cost[N]
while nowt>0:
    for i in adj[nowp]:
        if cost[i]==nowt-1:
            root.append(i)
            nowp=i
            nowt=nowt-1
            break