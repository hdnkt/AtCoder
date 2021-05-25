#dp[i][j]:i日目に活動j:0,1,2:A,B,Cをするときの幸福度の最大値

N = int(input())
abc = [list(map(int,input().split())) for i in range(N)]#abc:012

dp = [[0,0,0] for i in range(0,N,1)]
dp[0] = abc[0]

for i in range(1,N,1):
    for j in range(0,3,1):#012:abc
        dp[i][j] = abc[i][j]+max(dp[i-1][(j+1)%3],dp[i-1][(j+2)%3])

print(max(dp[N-1]))