N=int(input())

A = list(map(int,input().split()))

pre = []
if N%2==1:
    pre.append(0)

for i in range(0,N//2):
    pre.append(2*i+N%2+1)
    pre.append(2*i+N%2+1)

A.sort()
#無理なもんは無理
for i in range(N):
    if A[i]!=pre[i]:
        print(0)
        exit()

#そうでないなら
print(pow(2,(N//2),10**9+7))