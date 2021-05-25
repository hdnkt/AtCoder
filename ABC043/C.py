N = int(input())

a = list(map(int,input().split()))

x = sum(a)//N

ans1 = 0
for i in range(N):
    ans1+=(x-a[i])*(x-a[i])

x=x+1
ans2 = 0
for i in range(N):
    ans2+=(x-a[i])*(x-a[i])

print(min(ans1,ans2))