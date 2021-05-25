N = int(input())
a = list(map(int,input().split()))
a.sort()
c = 1
l= int(a[N-1]**(1/(N-1)))
r= l+1

scorel = 0
for i in range(N):
    scorel += abs(a[i]-l**i)

scorer = 0
for i in range(N):
    if r**i > 10**15:
        break
    scorer += abs(a[i]-r**i)

print(min(scorer,scorel))


