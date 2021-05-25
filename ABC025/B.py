N,A,B = map(int,input().split())

sd = [input().split() for i in range(N)]

ans = 0

for i in range(N):
    s,d = sd[i]
    d = int(d)

    d = min(d,B)
    d = max(d,A)

    if s == "East":
        d = d
    else:
        d =-d
    
    ans += d

if ans < 0:
    print("West "+str(-ans))
elif ans > 0:
    print("East "+str(ans))
else:
    print(0)
