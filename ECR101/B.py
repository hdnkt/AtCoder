T = int(input())

ans = []
for t in range(T):
    n = int(input())
    a = [0]+list(map(int,input().split()))
    m = int(input())
    b = [0]+list(map(int,input().split()))
    for i in range(1,n+1):
        a[i]=a[i]+a[i-1]
    for i in range(1,m+1):
        b[i]=b[i]+b[i-1]
    
    ans.append(max(a)+max(b))

for i in range(T):
    print(ans[i])
