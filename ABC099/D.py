import itertools

N,C =map(int,input().split())
D = [0]+[[0]+list(map(int,input().split())) for i in range(C)]

c = [list(map(int,input().split())) for i in range(N)]

grids = [[],[],[]]#振り分ける
for i in range(N):
    for j in range(N):
        grids[(i+j)%3].append(c[i][j])

iwa = [[0]*(C+1) for i in range(3)]#grids[i]を色jにした時の違和感

for i in range(3):
    for j in range(1,C+1,1):
        for k in range(len(grids[i])):
            iwa[i][j]+=D[grids[i][k]][j]

ans = float("inf")
for bits in itertools.permutations(list(range(1,C+1)),3):
    tmpans = 0
    for i in range(3):
        tmpans +=iwa[i][bits[i]]
    ans = min(tmpans,ans)

print(ans)