N,D,K = map(int,input().split())
LR = [list(map(int,input().split())) for i in range(D)]
ST = [list(map(int,input().split())) for i in range(K)]

ans = []

for i in range(K):
    nowL,nowR=ST[i][0],ST[i][0]
    goal = ST[i][1]
    for j in range(D):
        l,r = LR[j]
        if (l<=nowL and nowL<=r)or(l<=nowR and nowR<=r):
            nowL=min(nowL,l)
            nowR=max(nowR,r)
        if nowL<=goal and goal<=nowR:
            ans.append(j+1)
            break 

for i in range(K):
    print(ans[i])