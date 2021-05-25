N = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)

ansA=0
ansB=0
for i in range(N):
    if i%2==0:
        ansA+=a[i]
    else:
        ansB+=a[i]

print(ansA-ansB)