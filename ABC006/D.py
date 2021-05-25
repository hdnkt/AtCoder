INF = 10**10

N = int(input())
c = [int(input()) for i in range(N)]
dp = [INF for i in range(N)]
import bisect
for i in range(N):
    tmp = bisect.bisect(dp,c[i])
    dp[tmp]=c[i]
ans = 0
for i in range(N):
    if dp[i]!=INF:
        ans+=1
print(N-ans)