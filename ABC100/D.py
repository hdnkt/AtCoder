N,M = map(int,input().split())

xyz = [list(map(int,input().split())) for i in range(N)]

ans = 0

if M == 0:
    print(0)
    exit()

import itertools
for kum in itertools.product([-1,1],repeat=3):#8
    #dp[i][j]:i個目までの中でj個選んだ時の最大スコア
    dp=[[-10**15 if j!=0 else 0 for j in range(M+1)] for i in range(N)]
    tmp = 0
    for k in range(3):
        tmp+=kum[k]*xyz[0][k]
    dp[0][1]=tmp

    for i in range(1,N):
        tmp = 0
        for k in range(3):
            tmp+=kum[k]*xyz[i][k]
    
        for j in range(M+1):
            #iこめを選ばない
            dp[i][j]=max(dp[i-1][j],dp[i][j])
            #i個目を選ぶ
            if 0<=j-1:
                dp[i][j]=max(dp[i-1][j-1]+tmp,dp[i][j])
    
    ans = max(ans,dp[N-1][M])

print(ans)
