N,K = map(int,input().split())
xy = []

a = [[0]*(K+1) for i in range(K+1)]
b = [[0]*(K+1) for i in range(K+1)]
btotal=0

for i in range(N):
    x,y,c = input().split()
    x=int(x)
    y=int(y)
    if c == "B":
        y-=K
    x%=2*K
    y%=2*K

    if y >= K:
        x=(x+K)%(2*K)
        y-=K
    xy.append([x,y])
    if x>=K:
        x=x-K
        b[x][y]+=1
        btotal+=1
    else:
        a[x][y]+=1

ruisekiA = [[0]*(K+1) for i in range(K+1)]
ruisekiB = [[0]*(K+1) for i in range(K+1)]
#２次元累積
for i in range(K):
    for j in range(K):
        ruisekiA[i+1][j+1]=ruisekiA[i][j+1] + ruisekiA[i+1][j] - ruisekiA[i][j] + a[i][j]
        ruisekiB[i+1][j+1]=ruisekiB[i][j+1] + ruisekiB[i+1][j] - ruisekiB[i][j] + b[i][j]

def q(x,y,x2,y2,ruiseki):
    if x < 0 or y<0:
        return 0
    return ruiseki[x][y]+ruiseki[x2][y2]-ruiseki[x][y2]-ruiseki[x2][y]

ans = 0
for i in range(K+1):
    for j in range(K+1):
        atemp=0
        atemp += q(i,j,K,K,ruisekiA)
        atemp += q(0,0,i,j,ruisekiA)
        btemp=0
        btemp += q(i,j,K,K,ruisekiB)
        btemp += q(0,0,i,j,ruisekiB) 
        btemp=btotal-btemp
        tempans=atemp+btemp
        ans=max(ans,tempans)

        atemp=0
        atemp += q(i,j,K,K,ruisekiA)
        atemp += q(0,0,i,j,ruisekiA)
        btemp=0
        btemp += q(i,j,K,K,ruisekiB)
        btemp += q(0,0,i,j,ruisekiB) 
        atemp= N - btotal - atemp
        tempans=atemp+btemp
        ans=max(ans,tempans)      

print(ans)