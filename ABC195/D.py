N,M,Q = map(int,input().split())
wv = [list(map(int,input().split()))+[0] for i in range(N)]
X = list(map(int,input().split()))

Que = [list(map(int,input().split())) for i in range(Q)]

ans = []
for i in range(Q):
    for j in range(N):
        wv[j][2]=0

    l,r = Que[i]
    bags = X[0:l-1]+X[r:M]
    bags.sort()

    tmpans = 0

    for j in range(len(bags)):
        zantei = -1
        zanteiV = 0
        zanteiW = 0
        for k in range(N):
            if wv[k][2]==1 or wv[k][0]>bags[j]:
                continue
            if zantei == -1 or zanteiV < wv[k][1]:
                zantei=k
                zanteiV=wv[k][1]
                zanteiW=wv[k][0]
            elif zanteiV==wv[k][1]:
                if zanteiW < wv[k][0]:
                    zantei=k
                    zanteiV=wv[k][1]
                    zanteiW=wv[k][0]
        tmpans+=zanteiV
        if zantei != -1:
            wv[zantei][2]=1

    print(tmpans)



