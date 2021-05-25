N,M = map(int,input().split())
A = [0]*(M+2)#その宝石をとらないときのハイスコア
#を最終的にいれるためにいもす法

total = 0

for i in range(N):
    l,r,s=map(int,input().split())
    total+=s

    A[l]-=s
    A[r+1]+=s

for i in range(1,M+2):
    A[i]=A[i]+A[i-1]

ans = max(A[1:M+1])
ans = total+ans

print(ans)