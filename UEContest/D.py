N,X = map(int,input().split())

PS = [list(map(int,input().split())) for i in range(N)]
PS.sort()

ans = 0
for i in range(N):

    p,s = PS[i]

    if s >= X:
        ans += p*X
        break
    else:
        ans += p*s
        X -= s

print(ans)
