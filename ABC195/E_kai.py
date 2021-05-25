N = int(input())
S = list(map(int,list(input())))
X = list(input())

dic = {"T":1,"A":0}
X = [dic[X[i]] for i in range(N)]

dp = [[0 for j in range(7)]for i in range(N+1)]
dp[N][0]=1

for i in range(N-1,-1,-1):
    if X[i]==1:#高橋君のターン
        for j in range(7):
            a = (10*j)%7
            b = (10*j+S[i])%7
            if dp[i+1][a]==0 and dp[i+1][b]==0:
                dp[i][j]=0
            else:
                dp[i][j]=1
    else:
        for j in range(7):
            a = (10*j)%7
            b = (10*j+S[i])%7
            if dp[i+1][a]==1 and dp[i+1][b]==1:
                dp[i][j]=1
            else:
                dp[i][j]=0

print("Takahashi" if dp[0][0]==1 else "Aoki")