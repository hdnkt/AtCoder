N = int(input())
d = [int(input()) for i in range(N)]

d.sort(reverse=True)

ans = 0
tmp = 100000
for i in range(N):
    if d[i]<tmp:
        ans+=1
        tmp=d[i]
print(ans)