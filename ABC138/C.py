N = int(input())
v = list(map(int,input().split()))
v.sort()

ans=v[0]
for i in range(0,N,1):
    ans = (ans+v[i])/2
print(ans)
