N = int(input())
c = list(input())

rcount =0
wcount =0
for i in range(N):
    if c[i]=="R":
        rcount+=1
    else:
        wcount+=1

ans = 0
for i in range(rcount):
    if c[i]=="W":
        ans+=1

print(ans)