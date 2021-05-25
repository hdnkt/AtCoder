N,M = map(int,input().split())
A = list(map(int,input().split()))

dic = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
A.sort(reverse=True)
check = [0 for i in range(10)]

lis = []
#上位互換があるなら消す
base = A[0]
mi = dic[A[0]]
for i in A:
    if check[dic[i]]==0:
        lis.append([i,dic[i]])
        check[dic[i]]=1
        if mi >= dic[i]:
            base = i
            mi = dic[i]

for i in range(len(lis)):
    lis[i][1]-=mi


keta = N//mi
tmp = N%mi
print(tmp)
while 1:
    #dp[i][j]:iまでみて、j本使って
    dp = [[0 if j==0 else -1 for j in range(tmp+1)]for i in range(len(lis)+1)]
    for i in range(1,len(lis)+1):
        if lis[i-1][1]==0:
            for j in range(tmp+1):
                dp[i][j]=dp[i-1][j]
            continue
        for k in range(1,tmp//lis[i-1][1]+1):
            for j in range(k*lis[i-1][1],tmp+1):
                print(j,k*lis[i-1][1])
                dp[i][j]=max(dp[i-1][j-k*lis[i-1][1]]+k*(lis[i-1][0]-base),dp[i][j])
    
    #if dp[len(lis)][tmp]!=-1:
    print(dp)
    break
    keta-=1
    tmp+=mi
