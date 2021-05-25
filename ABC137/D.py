from heapq import heapify,heappop,heappush

N,M = map(int,input().split())
AB=[]

for i in range(0,N,1):
    a,b= map(int,input().split())
    AB.append([a,b])

AB.sort()
q = []
heapify(q)
cersol = 0
ans = 0
for i in range(0,M+1,1):#残り日数
    while 1:
        if cersol < N and AB[cersol][0] <= i:
            heappush(q,-AB[cersol][1])
            cersol+=1
        else:
            break
    if len(q)>0:
        ans += -heappop(q)
print(ans)

