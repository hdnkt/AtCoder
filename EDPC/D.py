#dp[i][j]:i番目までの品物の中で重さj以下になるように持った時の価値
#最終的な答えに沿うようにここは決める

N,W = map(int,input().split())
wv = [list(map(int,input().split())) for i in range(N)]#wv:01

dp = [[0]*(W+1) for i in range(0,N,1)]
for i in range(wv[0][0],W+1,1):#一番左の荷物に関しては自明なので
    dp[0][i]=wv[0][1]

for i in range(1,N,1):
    for j in range(0,W+1,1):
        dp[i][j]=max(dp[i-1][j],dp[i][j])
        if j - wv[i][0] >= 0:
            dp[i][j]=max(dp[i-1][j-wv[i][0]]+wv[i][1],dp[i][j])
print(dp[N-1][W])