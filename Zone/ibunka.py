N,M = map(int,input().split())

adj = [[] for i in range(N)]

for i in range(M):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

import itertools

ma = 0
ans = [0,0,0]

for it in itertools.combinations(list(range(N)),3):
    tmp = {}
    for i in range(3):
        for j in range(len(adj[it[i]])):
            tmp[adj[it[i]][j]]=0
    tmp = list(tmp)

    if ma < len(tmp):
        ma = len(tmp)
        ans = list(it)
        print(it,tmp)

print()
for i in range(N):
    print(adj[i])
print(ans)