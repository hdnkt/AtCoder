def de(n):
    return int(n)-1

H,W,N = map(int,input().split())
ab = [list(map(de,input().split())) for i in range(N)]
dic = {}
for i in range(N):
    a,b = ab[i]
    dic[tuple([a,b])]=1

ans = [0 for i in range(10)]

for i in range(N):
    a,b = ab[i]
    #どこを中心とするか
    for p in range(-1,2,1):
        j = a+p
        if j<=0 or H-1<=j:
            continue
        for f in range(-1,2,1):
            k = b+f
            if k<=0 or W-1<=k:
                continue

            #何個含まれているか
            tmpans = 0
            for l in range(-1,2,1):
                for m in range(-1,2,1):
                    if tuple([j+l,k+m]) in dic:
                        tmpans+=1
            ans[tmpans]+=1
    
for i in range(1,10):
    ans[i]=ans[i]//i

ans[0]=(H-2)*(W-2)-sum(ans)

for i in range(10):
    print(ans[i])
