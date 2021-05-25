S = list(input())
N = int(input())

S.sort()

ans = []

for i in range(5):
    for j in range(5):
        ans.append(S[i]+S[j])

print(ans[N-1])
