def henk(s):
    if s == "G":
        return 0
    else:
        return int(s)

a,b,n = map(int,input().split())

p = list(map(henk,input().split()))

ans = 0

throw = 0
B = b
for i in range(n):
    throw += 1
    broken = p[i]
    B = B-broken

    ans += broken
    if B == 0:
        if throw == 1:#ストライク
            if i+1 < n:
                ans+=p[i+1]
            if i+2 < n:
                ans+=p[i+2]
            throw=0
            B = b
        elif throw == 2:#スペア
            if i+1 < n:
                ans+=p[i+1]
            throw=0
            B = b
    
    if throw==2:
        throw=0
        B = b

print(ans)