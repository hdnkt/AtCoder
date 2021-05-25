N = int(input())

T = list(map(int,input().split()))

M = int(input())

ans = []
buckup = sum(T)
tmp = buckup
for i in range(M):
    p,x=map(int,input().split())
    p-=1
    tmp=buckup
    tmp+=x-T[p]
    ans.append(tmp)

for i in range(M):
    print(ans[i])

