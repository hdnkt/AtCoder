N,M,P,Q,R = map(int,input().split())

choc = [[] for i in range(N)]
for i in range(R):
    x,y,z = map(int,input().split())
    choc[x-1].append([z,y-1])

ans=0
from itertools import combinations
for p in combinations(list(range(N)),P):
    point = [0]*(M)
    for i in p:
        for t in choc[i]:
            point[t[1]]+=t[0]
    point.sort(reverse=True)
    ans = max(ans,sum(point[0:Q]))

print(ans)