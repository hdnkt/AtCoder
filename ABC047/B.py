W,H,N=map(int,input().split())

l=0
r=W
d=0
u=H
for i in range(N):
    x,y,a=map(int,input().split())
    if a==1:
        l=max(l,x)
    elif a==2:
        r=min(r,x)
    elif a==3:
        d=max(d,y)
    elif a==4:
        u=min(u,y)

ans = max(0,u-d)*max(0,r-l)

print(ans)