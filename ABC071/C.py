from heapq import heapify,heappush,heappop#最小（最大）の値をlogNで取り出せる。（値の追加もlogN）
a = []
heapify(a)

dic = {}

N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    if not(A[i] in dic):
        dic[A[i]]=1
    elif dic[A[i]]==1:
        dic[A[i]]=0
        heappush(a,-A[i])
    elif dic[A[i]]==0:
        dic[A[i]]=1

if len(a)<2:
    print(0)
    exit()

w = heappop(a)
h = heappop(a)

print(w*h)
