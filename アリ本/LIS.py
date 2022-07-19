#配列を渡すと最大増加列の長さを返す
#列そのものを返してほしかったらdpを適当に切って渡せ
import bisect
def LIS(c):
    N = len(c)
    INF = 10**10
    dp = [INF for i in range(N)]
    for i in range(N):
        # 単調増加<:bisect_left 広義単調増加<=:bisect
        tmp = bisect.bisect_left(dp,c[i])
        dp[tmp]=c[i]
    return bisect.bisect_left(dp,INF-1)

#ABC006 D
N = int(input())
c = [int(input()) for i in range(N)]
print(LIS(c))