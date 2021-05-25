import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)


N = int(input())

ans = 1
for i in range(2,N+1):
    ans = lcm(ans,i)

print(ans+1)