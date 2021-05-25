N,x = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
if a[0]>x:
    ans+=a[0]-x
    a[0]=x

for i in range(1,N):
    if a[i]+a[i-1]>x:
        ans+=a[i]-x+a[i-1]
        a[i]=x-a[i-1]

print(ans)