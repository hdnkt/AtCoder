N,M = map(int,input().split())

# b[n] = ノードnからの流出先ノードの集合のbitフラグ
b = [0 for i in range(N)]

for i in range(M):
    x,y = map(int,input().split())
    x -=1
    y -=1
    b[x]= b[x]|pow(2,y)

 
dp = [0] * (1 << N)
dp[0] = 1
# ノードIDと対応するビット位置は繰り返し求めるので事前計算しておく
jbs = [(j, 1 << j) for j in range(N)]
 
for i in range(1 << N):
    for j, jb in jbs:
        if (i & jb) == 0 and (i & b[j]) == 0:
            dp[i | jb] += dp[i]
 
print(dp[-1])

