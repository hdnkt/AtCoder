N = int(input())
A = list(map(int,input().split()))

cap = [1]*(N+1)#0-N

if A[0] > 1 or (A[0]==1 and N !=0):
    print(-1)
    exit()

for i in range(1,N+1,1):#1-N
    cap[i]=cap[i-1]*2 - A[i]
    if cap[i] < 0 or (cap[i]==0 and i!=N):
        print(-1)
        exit()

T = [0]*(N+1)
T[N]=A[N]#ここのキャパオーバーは上ではじけるはず
for i in range(N-1,-1,-1):
    T[i]=A[i]+min(T[i+1],cap[i])

print(sum(T))


