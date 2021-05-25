from heapq import heapify,heappop,heappush

N,Q = map(int,input().split())
enji = [0]*(N+1)

youchien = [[] for i in range(0,2*(10**5)+1,1)]
youchien_deleted = [[] for i in range(0,2*(10**5)+1,1)]
for i in range(0,2*(10**5)+1,1):
    heapify(youchien[i])
    heapify(youchien_deleted[i])

for i in range(1,N+1,1):
    a,b = map(int,input().split())
    heappush(youchien[b],[-a,i])
    enji[i]=b

saikyou = []
saikyou_delieted = []
for i in range(0,2*(10**5)+1,1):
    if len(youchien[i])>0:
        heappush(saikyou, [-youchien[i][0][0],youchien[i][0][1],i])


def deletCheck(enNum):#s:最強 e:園児
    while youchien[enNum][0]==youchien_deleted[enNum][0]:
        heappop(youchien[enNum])
        heappop(youchien_deleted[enNum])

def deletCheckSE():#s:最強 e:園児
    while saikyou[0]==saikyou_delieted[0]:
        heappop(saikyou)
        heappop(saikyou_delieted)

for i in range(0,Q,1):#ここからクエリ処理
    C,D = map(int,input().split())

    heappush(saikyou_delieted,[])

    heappush(youchien_deleted[enji[C]])

    enji[C]=D

