T = int(input())

ans = []
for t in range(T):
    N = int(input())
    dic = {}
    for i in range(N):
        s=list(input())
        for j in range(len(s)):
            if s[j] in dic:
                dic[s[j]]+=1
            else:
                dic[s[j]]=1
    
    ok = True
    for i in dic:
        if dic[i]%N != 0:
            ok=False
    ans.append("YES" if ok else "NO")

for i in range(T):
    print(ans[i])
