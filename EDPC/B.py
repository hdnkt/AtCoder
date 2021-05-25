INF = 10**12

N,K = map(int,input().split())
h = list(map(int,input().split()))

dp = [INF]*(N)
dp[0]=0
for i in range(1,N,1):
    for j in range(max(0,i-K),i,1):
        dp[i]= min(dp[i],dp[j]+abs(h[i]-h[j]))
print(dp[N-1])
