N,W = map(int,input().split())
v=[0]*N
w=[0]*N
for i in range(0,N,1):
    v[i],w[i]=map(int,input().split())

def allsearch(i,j):#i番目以降からjの重さまでで一番高い価値を返す.計算量2**n
    if i == N:
        return 0
    if j-w[i]>=0:
        return max([dp(i+1,j),dp(i+1,j-w[i])+v[i]])
    else:
        return dp(i+1,j)

mem = [[-1 for i in range(0,N,1)]for j in range(0,W+1,1)]
def dp(i,j):#都度記憶。計算量はiとjがとりうる値の数でN*W
    print(i,j)
    if i == N:
        return 0
    if mem[j][i] != -1:
        return mem[j][i]
    if j-w[i]>=0:
        mem[j][i] = max([dp(i+1,j),dp(i+1,j-w[i])+v[i]])
        return max([dp(i+1,j),dp(i+1,j-w[i])+v[i]])
    else:
        mem[j][i] = dp(i+1,j)
        return dp(i+1,j)
    

print(dp(0,W))