N = int(input())
a = list(map(int,input().split()))
if N ==1:
    print(1,1)
    print(-a[0])
    print(1,1)
    print(0)
    print(1,1)
    print(0)
    exit()

print(1,1)
print(-a[0])
a[0]=0

print(2,N)
ans = []
for i in range(1,N):
    ans.append((a[i]%N)*(N-1))
    a[i]=a[i]+(a[i]%N)*(N-1)
print(" ".join(list(map(str,ans))))

for i in range(N):
    a[i]=-a[i]
print(1,N)
print(" ".join(list(map(str,a))))

