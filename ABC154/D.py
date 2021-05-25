N,K = map(int,input().split())
p = list(map(int,input().split()))

for i in range(0,N,1):
    p[i] = (p[i]+1)/2

tmp = sum(p[0:K])
ans = tmp
for i in range(0,N-K,1):
    tmp -= p[i]
    tmp += p[K+i]
    ans = max(ans,tmp)

print(ans)
