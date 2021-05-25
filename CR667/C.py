T = int(input())

ret = []
for t in range(T):
    n,x,y = map(int,input().split())

    for k in range(1,50):
        if x%k != y%k:
            continue
        if not(x+k*(n-1)>=y):
            continue

        ans = [0]*(n)
        ans[0]=max(y-(n-1)*k,y%k)
        if ans[0]==0:
            ans[0]=k

        for i in range(1,n):
            ans[i]=ans[i-1]+k
        break
    
    ret.append(ans)

for t in range(T):
    print(" ".join(list(map(str,ret[t]))))

