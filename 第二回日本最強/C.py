A,B = map(int,input().split())

ma = B-A
ans = 1
for i in range(1,ma+1):
    l = A + i - A%i
    if A%i == 0:
        l = A
    r = l + i


    if A<=l and l<=B and A<=l and r<=B:
        ans = i

print(ans)