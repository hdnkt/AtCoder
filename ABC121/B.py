N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(N)]

ans = 0
for i in range(0,N,1):
    tmp=C
    for j in range(0,M,1):
        tmp+=A[i][j]*B[j]
    if tmp > 0:
        ans+=1
print(ans)