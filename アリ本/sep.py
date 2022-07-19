n,m = map(int,input().split())

dp = [[0 for j in range(0,n+1,1)] for i in range(0,m+1,1)]#[i][j]:=jのi分割

dp[0][0]=1

for i in range(1,m+1,1):
    for j in range(0,n+1,1):
        if j - i >=0:
            dp[i][j] = dp[i-1][j]+dp[i][j-i]
        else:
            dp[i][j] = dp[i-1][j]

print(dp)