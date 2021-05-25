N,S,T = map(int,input().split())

W = int(input())

ans = 0
tmp = W
for i in range(N-1):
    if tmp <= T and S<=tmp:
        ans+=1
    a = int(input())
    tmp = tmp+a
if tmp <= T and S<=tmp:
    ans+=1

print(ans)