import bisect
 
A, B, Q = map(int, input().split())
INF = float('inf')
s = [-INF] + [int(input()) for i in range(A)] + [INF]
t = [-INF] + [int(input()) for i in range(B)] + [INF]
 
for i in range(Q):
    x = int(input())
    b = bisect.bisect_right(s, x)
    d = bisect.bisect_right(t, x)
    ans = INF
    for S in [s[b-1], s[b]]:
        for T in [t[d-1], t[d]]:
            ans1 = abs(S-x) + abs(S-T)
            ans2 = abs(T-x) + abs(T-S)
            ans = min(ans, ans1, ans2)
    print(ans)