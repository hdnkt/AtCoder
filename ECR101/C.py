T = int(input())

ans = []
for t in range(T):
    flag = True
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    tmp = [0]*(n)
    tmp[0]=h[0]
    for i in range(1,n-1):
        ma = min(tmp[i-1]+k-1,h[i]+k-1)
        mi = max(tmp[i-1]-k+1,h[i])
        if mi > ma:
            flag = False
        if h[i+1]>h[i]:
            tmp[i]=ma
        else:
            tmp[i]=mi
    
    if abs(h[n-1]-tmp[n-2])>=k:
        flag =False
    
    ans.append("YES" if flag else "NO")

for i in range(T):
    print(ans[i])