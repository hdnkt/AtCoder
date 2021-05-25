from collections import Counter

N = int(input())
s = [list(input()) for i in range(0,N,1)]
for i in range(0,N,1):
    s[i].sort()
S = ["".join(s[i]) for i in range(0,N,1)]

cnt = Counter(S)
ans =0
for i in set(S):
    ans += cnt[i]*(cnt[i]-1)//2
print(ans)
