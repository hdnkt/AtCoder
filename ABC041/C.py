N = int(input())
a = list(map(int,input().split()))

a = [[a[i],i] for i in range(N)]

a.sort(reverse=True)
for i in range(N):
    print(a[i][1]+1)
