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

#aからの距離をレベルとして持つ

MOD = 10**9+7

N = int(input())
a,b=map(int,input().split())
a-=1
b-=1
M=int(input())
xy = [list(map(int,input().split())) for i in range(M)]

adj_list = [[]for i in range(N)]
for i in range(M):
    x,y=xy[i]
    x-=1
    y-=1
    adj_list[x].append([y,1])
    adj_list[y].append([x,1])

ans = dijk(a,adj_list)

st = [[ans[i],i] for i in range(N)]
stt = [st[i]for i in range(N)]
st.sort()

dp = [0 for i in range(N)]
dp[a]=1

for i in range(N):
    tmplevel,tmp = st[i]
    for j in range(len(adj_list[tmp])):
        if ans[adj_list[tmp][j][0]]>tmplevel:
            dp[adj_list[tmp][j][0]]+=dp[tmp]
            dp[adj_list[tmp][j][0]]%=MOD

print(dp[b])

