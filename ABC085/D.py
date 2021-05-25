import math

N,H = map(int,input().split())

A=[]
B=[]

for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

maxA = max(A)
B.sort(reverse=True)


nage = 0
ans = math.ceil((H+maxA)/maxA)#投げなし
for i in range(N):
    nage+=B[i]
    ans = min(ans, (i+1) + math.ceil((max(0,H-nage))/maxA))

print(ans)