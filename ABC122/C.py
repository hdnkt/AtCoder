N,Q = map(int,input().split())
S = ["N"] + list(input())

A_ruiseki = [0 for i in range(N+1)]
C_ruiseki = [0 for i in range(N+1)]

for i in range(0,N,1):
    if S[i]=="A" and S[i+1]=="C":
        A_ruiseki[i]+=1
        C_ruiseki[i+1]+=1

for i in range(1,N+1,1):
    A_ruiseki[i]+=A_ruiseki[i-1]
    C_ruiseki[i]+=C_ruiseki[i-1]

ans = []
for i in range(Q):
    l,r = map(int,input().split())
    A = A_ruiseki[r]-A_ruiseki[l-1]
    C = C_ruiseki[r]-A_ruiseki[l-1]
    ans.append(min(A,C))

for i in range(Q):
    print(ans[i])