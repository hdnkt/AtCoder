N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = []
for i in range(N):
    if not(A[i] in B):
        ans.append(A[i])

for i in range(M):
    if not(B[i] in A):
        ans.append(B[i])

ans.sort()
print(" ".join(list(map(str,ans))))
