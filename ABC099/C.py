N = int(input())

ans = 100000
for i in range(0,N+1,1):#i円6で払うj円9で払う
    j = N - i

    icount = 0
    while i!=0:
        icount += (i%6)
        i=i//6

    jcount = 0
    while j!=0:
        jcount += (j%9)
        j=j//9

    ans = min(icount+jcount,ans)

print(ans)