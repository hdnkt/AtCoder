import math
H,N = map(int,input().split())
A=[]
B=[]
for i in range(0,N,1):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

dp = [[0 for j in range(0,H+1,1)]for i in range(0,N,1)]

for j in range(0,H+1,1):#初期化
    dp[N-1][j]=B[N-1]*math.ceil(j/A[N-1])

for i in range(0,N,1):#初期化２
    dp[i][0]=0

for i in range(N-2,-1,-1):
    for j in range(0,H+1,1):
        if j-A[i] >= 0:
            dp[i][j]=min(dp[i+1][j],dp[i][j-A[i]]+B[i])
        else:
            dp[i][j]=min(dp[i+1][j],B[i])

print(dp[0][H])