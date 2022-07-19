n,k = map(int,input().split())
a = list(map(int,input().split()))
m = list(map(int,input().split()))

dp = [[False for i in range(0,n+1,1)]for j in range(0,k+1,1)]#i番目までを使ってjを作れるか
dp[0][0] =True
for i in range(0,n,1):
    for j in range(0,k+1,1):
        for p in range(0,m[i]+1,1):
            if dp[j-p*a[i]][i] and j-p*a[i]>=0:
                dp[j][i+1] = True

print(dp[k][n])