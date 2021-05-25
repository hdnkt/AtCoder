n,D,H = map(int,input().split())

ans = 0
for i in range(n):
    d,h = map(int,input().split())
    tmp = H - D*(H-h)/(D-d)
    ans = max(ans,tmp)

print(ans)