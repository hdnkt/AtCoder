# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
# 場合によっては再帰上限替えないとダメかも

import sys
sys.setrecursionlimit(10000000)

def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

N,M = map(int,input().split())
G = [[] for i in range(N)]
RG = [[] for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    RG[b].append(a)

label,group = scc(N,G,RG)

dic = {}
for i in group:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

ans = 0
for i in dic:
    ans+=dic[i]*(dic[i]-1)//2

print(ans)