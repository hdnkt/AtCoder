n,q = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

from heapq import heapify,heappush,heappop

que = []
heapify(que)
dic = {}

queL = []
queR = []
heapify(queL)
heapify(queR)
for i in range(n):
    heappush(queL,a[i])
    heappush(queR,-a[i])#でかい方から取り出したいから-
    dic[a[i]]=0
for i in range(1,n):#でかい方から取り出したいから-
    heappush(que,[-a[i]+a[i-1],a[i],a[i-1]])

ret = []
ans = que[0]-(-queR[0]-queL[0])
ret.append(ans)

for query in range(q):
    x,y = map(int,input().split())
    if x == 0:
        dic.pop(y)
    else:
        dic[y]=0
        heappush(queL,y)
    
    length,L,R = heappop(que)
    while not((L in dic)and(R in dic)):
        length,L,R = heappop(que)
    heappush(que,[length,L,R])
    length = -length

    l = heappop(queL)
    while not(l in dic):
        l = heappop(queL)
    heappush(queL,l)

    r = heappop(queR)
    while not(r in dic):
        r = heappop(queR)
    heappush(queL,r)
    r = -r

    ret.append(r-l-length)


    
