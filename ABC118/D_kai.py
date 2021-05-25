N,M = map(int,input().split())
A = list(map(int,input().split()))

dic = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
A.sort(reverse=True)
#i本使うときの可能最大桁数
dp=[-1 if i != 0 else 0 for i in range(N+1)]
for i in range(1,N+1):
    for j in A:
        if i-dic[j]>=0 and dp[i-dic[j]]>=0:
            dp[i]=max(dp[i],dp[i-dic[j]]+1)
#dp[i]-1=dp[i-dic[x]] なら最高位の桁にxを使える
now = N
ans = []
for i in range(dp[N]-1):
    for j in A:
        if dp[now]-1==dp[now-dic[j]]:
            ans.append(j)
            now = now-dic[j]
            break
for j in A:
    if now-dic[j]==0:
        ans.append(j)
        now = now-dic[j]
        break

print("".join(list(map(str,ans))))