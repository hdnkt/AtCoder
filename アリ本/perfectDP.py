N,W = map(int,input().split())#ナップザック問題
v=[0]*N
w=[0]*N
for i in range(0,N,1):
    v[i],w[i]=map(int,input().split())

mem = [[0 for i in range(0,N+1,1)]for j in range(0,W+1,1)]

for i in range(N-1,-1,-1):
    for j in range(0,W+1,1):
        if j-w[i] < 0:
            mem[j][i] = mem[j][i+1]
        else:
            mem[j][i] = max([mem[j][i+1],mem[j-w[i]][i+1]+v[i]])

print(mem[W][0])