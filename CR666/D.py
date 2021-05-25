T = int(input())

ans = []
for t in range(T):
    N = int(input())
    a = list(map(int,input().split()))
    if N ==1:
        ans.append("T")
    else:
        ans.append("T" if sum(a)%2 == 1,)