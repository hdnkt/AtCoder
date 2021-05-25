N = int(input())

ans = True
preT,preX,preY = 0,0,0
for i in range(N):
    t,x,y = map(int,input().split())

    if abs(x-preX)+abs(y-preY) > t - preT:
        ans=False
    if (-abs(x-preX)-abs(y-preY) + t - preT)%2==1:
        ans=False
    
    preX = x
    preY = y
    preT = t

print("Yes" if ans else "No") 