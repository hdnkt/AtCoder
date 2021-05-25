from heapq import heapify,heappop,heappush

N,Q = map(int,input().split())
enji = [0]*(N+1)
rate = [0]*(N+1)
youchien = [[] for i in range(0,2*(10**5)+1,1)]

for i in range(0,2*(10**5)+1,1):
    heapify(youchien[i])

for i in range(1,N+1,1):
    a,b = map(int,input().split())
    heappush(youchien[b],[-a,i])
    enji[i]=b
    rate[i]=a

saikyou = []
for i in range(0,2*(10**5)+1,1):
    if len(youchien[i])>0:
        heappush(saikyou, [-youchien[i][0][0],youchien[i][0][1]])


ans = [0]*Q
for i in range(0,Q,1):
    C,D = map(int,input().split())

    cfrom = enji[C]
    enji[C] = D

    while youchien[cfrom]:
        if enji[youchien[cfrom][0][1]] != cfrom:
            heappop(youchien[cfrom])
        else:
            heappush(saikyou,[-youchien[cfrom][0][0],youchien[cfrom][0][1]])
            break
    
    heappush(youchien[D],[-rate[C],C])
    while youchien[D]:
        if enji[youchien[D][0][1]] != D:
            heappop(youchien[D])
        else:
            heappush(saikyou,[-youchien[D][0][0],youchien[D][0][1]])
            break

    while saikyou:
        if youchien[enji[saikyou[0][1]]][0][0] != -saikyou[0][0]:
            heappop(saikyou)
            continue
        else:
            ans[i] = saikyou[0][0]
            break

for i in range(Q):
    print(ans[i])