from math import gcd

N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(0,N,1):
    ans = gcd(ans,A[i])
print(ans)