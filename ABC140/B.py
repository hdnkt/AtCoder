N = int(input())
A = [0] + list(map(int,input().split()))
B = [0] + list(map(int,input().split()))
C = [0] + list(map(int,input().split()))
ans=0
pre = -2
for i in range(1,N+1,1):
    ans += B[A[i]]
    if A[i]-pre == 1:
        ans+=C[pre]
    pre = A[i]
print(ans)
