#dp[i][j]:iまでで価値jになるようにするときの品物の重さ
#答えはdp[N]をjが大きいものから見ていってWより小さいもの

INF = 10**15

N,W = map(int,input().split())
w = []
v = []
for i in range(N):
    tmpW,tmpV = map(int,input().split())
    w.append(tmpW)
    v.append(tmpV)

dp = [[INF]*(100*1000+1) for i in range(N)]
dp[0][0]=0
dp[0][v[0]]=w[0]

for i in range(1,N,1):
    for j in range(0,100*1000+1,1):
        dp[i][j] = min(dp[i-1][j],dp[i][j])
        if j - v[i]>=0:
            dp[i][j] = min(dp[i][j],dp[i-1][j-v[i]]+w[i])

for j in range(100*1000,-1,-1):
    if dp[N-1][j] <= W:
        print(j)
        exit()