import math

N = int(input())
ans = int(input())
for i in range(N-1):
    t = int(input())
    ans = t*ans//math.gcd(t,ans)
print(ans)
