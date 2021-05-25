Q = int(input())

ans = []
for i in range(Q):
    N = int(input())
    S = list(input())
    tmpans = []
    for i in range(N):
        tmpans.append(S[i+i])
    ans.append("".join(tmpans))

for i in range(Q):
    print(ans[i])
