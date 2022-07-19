N = int(input())
ans = []
dic = {}
for i in range(1,N+1):
    S = input()
    if not(S in dic):
        ans.append(i)
    dic[S]=0

for i in range(len(ans)):
    print(ans[i])