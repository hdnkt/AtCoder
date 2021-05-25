from collections import deque 
#スタック
s = deque([])

N,M=map(int,input().split())
G = [[] for i in range(N+1)]

LRD = []
for i in range(M):
    L,R,D = map(int,input().split())
    G[L].append([R,D])
    G[R].append([L,-D])

ans = True
X = [None]*(N+1)
for i in range(1,N+1):

    if X[i]==None:
        s.append([i,0])

    while len(s)>0:#dfs
        j,x = s.pop()
        if X[j]==None:
            X[j]=x
            for nex in G[j]:
                s.append([nex[0],x+nex[1]])
        else:
            if X[j]!=x:
                ans = False
                break

print("Yes" if ans else "No")
