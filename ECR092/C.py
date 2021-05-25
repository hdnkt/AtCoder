T = int(input())

ret = []
for t in range(T):
    n = int(input())
    a = [0]+list(map(int,input().split()))

    dpM = [10**7]*(n+1)
    dpF = [10**7]*(n+1)
    #そこを倒すのに必要な最小のスキップポイント(1-index)

    dpM[0]=0
    for i in range(1,n+1):
        dpF[i]=min(dpF[i],dpM[i-1]+a[i])
        dpF[i]=min(dpF[i],dpM[i-2]+a[i]+a[i-1])

        dpM[i]=min(dpM[i],dpF[i-1])
        dpM[i]=min(dpM[i],dpF[i-2])
    

    ret.append(min(dpF[n],dpM[n]))

for t in range(T):
    print(ret[t])
