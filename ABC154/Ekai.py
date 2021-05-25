def nCk(n,k):
    res = 1
    for i in range(k,0,-1):
        res = res*(n+1-i)/i
    return int(res)

N = input()
K = int(input())
ans = 0
dp_mikakutei = [[0 for i in range(0,K+1,1)] for j in range(0,len(N),1)]#Nより小さいかまだわからん
dp_kakutei = [[0 for i in range(0,K+1,1)] for j in range(0,len(N),1)]

dp_mikakutei[0][1]=1#その桁がまさにNのその桁と同じ
dp_kakutei[0][0]=1
dp_kakutei[0][1]=int(N[0])-1#1~N[0]-1

for i in range(1,len(N),1):
    dp_kakutei[i][0]=dp_kakutei[i-1][0] + dp_mikakutei[i-1][0]
    for j in range(1,K+1,1):
        if N[i] =="0":
            dp_mikakutei[i][j] = dp_mikakutei[i-1][j]
            dp_kakutei[i][j] = 9*dp_kakutei[i-1][j-1] +dp_kakutei[i-1][j]
        else:
            dp_mikakutei[i][j] = dp_mikakutei[i-1][j-1]
            dp_kakutei[i][j] = 9*dp_kakutei[i-1][j-1] + (int(N[i])-1)*dp_mikakutei[i-1][j-1] + dp_kakutei[i-1][j] + dp_mikakutei[i-1][j]
print(dp_mikakutei[len(N)-1][K] + dp_kakutei[len(N)-1][K])
