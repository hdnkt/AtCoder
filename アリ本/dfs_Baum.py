import sys
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
N_path=[[] for i in range(0,N,1)]

for i in range(0,M,1):
    u,v=map(int,input().split())
    N_path[u-1].append(v-1)
    N_path[v-1].append(u-1)

N_already=[False]*N

def dfs(n,pN):
    if N_already[n]==True:
        return False
    N_already[n]=True

    for i in N_path[n]:
        if i != pN:
            if not dfs(i,n):
                return False
    return True
counter=0

for i in range(0,N,1):
    if N_already[i] == False:
        if dfs(i,-1):
            counter+=1
print(counter)