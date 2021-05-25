N,K,Q = map(int,input().split())
A = [K-Q]*(N+1)
for i in range(0,Q,1):
    A[int(input())]+=1
for i in range(1,N+1,1):
    print("Yes" if A[i] > 0 else "No")
