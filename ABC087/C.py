N = int(input())
A = [list(map(int,input().split())) for i in range(2)]

for i in range(1,N):
    A[0][i]=A[0][i]+A[0][i-1]

for i in range(N-2,-1,-1):
    A[1][i]=A[1][i]+A[1][i+1]

for i in range(N):
    A[0][i]+=A[1][i]

print(max(A[0]))