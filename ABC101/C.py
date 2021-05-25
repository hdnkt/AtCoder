N,K = map(int,input().split())
A = list(map(int,input().split()))

ans = (N-1)//(K-1)
if (N-1)%(K-1)!=0:
    ans+=1
print(ans)
