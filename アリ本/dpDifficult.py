N,M = map(int,input().split())
v=[0]*N
w=[0]*N
for i in range(0,N,1):
    v[i],w[i]=map(int,input().split())

dp=[[0 for i in range(0,N+1,1)]for j in range(0,M+1,1)]#個数制限なしナップザック(計算量大)
for i in range(N-1, -1,-1):
    for j in range(1,M+1,1):
        dp[j][i] = max([dp[j-k*w[i]][i+1] + k*v[i] for k in range(0,j//w[i] +1,1)])

print(dp[M][0])
