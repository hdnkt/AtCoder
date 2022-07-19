n,m=map(int,input().split())
a = list(map(int,input().split()))

dp = [[0 for i in range(0,n+1,1)]for j in range(0,m+1,1)]

for i in range(0,n+1,1):
    dp[i][0]=1

for i in range(1,n+1,1):
    for j in range(1,m+1,1):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]
        if j-1-a[i-1]>=0:
            dp[i][j] = dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1-a[i-1]]

print(dp[n][m])