from heapq import heapify,heappop,heappush
N,M = map(int,input().split())
A = list(map(lambda x:-x,map(int,input().split())))
heapify(A)
for i in range(0,M,1):
    tmp = heappop(A)
    heappush(A,-((-tmp)//2))
print(-sum(A))