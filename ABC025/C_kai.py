b = [list(map(int,input().split())) for i in range(2)]
c = [list(map(int,input().split())) for i in range(3)]

#-1まだ、0:〇 1:×
S = [[-1 for j in range(3)]for i in range(3)]

def score(S):
    retT=0
    retK=0
    for i in range(2):
        for j in range(3):
            if S[i][j]==S[i+1][j]:
                retT+=b[i][j]
            else:
                retK+=b[i][j]
    for i in range(3):
        for j in range(2):
            if S[i][j+1]==S[i][j]:
                retT+=c[i][j]
            else:
                retK+=c[i][j]
    return retT,retK

INF = -10**10
#状態とターン数
def sol(S,t):
    if t==10:
        return score(S)

    tmp = S[0]+S[1]+S[2]
    tmp = tuple(tmp)
    if tmp in dp:
        return dp[tmp]

    #先行ターン
    if t%2==1:
        retT,retK = INF,INF
        for i in range(3):
            for j in range(3):
                if S[i][j]==-1:
                    S[i][j]=0
                    T,K = sol(S,t+1)
                    if retT < T:
                        retT = T
                        retK = K
                    S[i][j]=-1
        dp[tmp]=(retT,retK)
        return retT,retK
    else:
        retT,retK = INF,INF
        for i in range(3):
            for j in range(3):
                if S[i][j]==-1:
                    S[i][j]=1
                    T,K = sol(S,t+1)
                    if retK < K:
                        retT = T
                        retK = K
                    S[i][j]=-1
        dp[tmp]=(retT,retK)
        return retT,retK

dp = {}
ans = sol(S,1)
print(ans[0])
print(ans[1])