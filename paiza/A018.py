def check(n):
    return 1 if n>=0 else -1

import math

W,H,M,N = map(int,input().split())


#監視カメラ読み込み
camera = [list(map(int,input().split())) for i in range(M)]

#美術品読み込み
#arts = [list(map(int,input().split())) for i in range(N)]

ansl = []

for i in range(N):
    x,y = map(int,input().split())

    ans = False
    for j in range(M):
        X,Y,T,D,R = camera[j]
        print(X,Y,T)
        tmpans = True
        #ダメな条件を満たしていないかチェック

        #Rより遠くにある
        if R*R < (X-x)*(Y-y):
            tmpans = False

        #下の線より下にある
        arc = math.radians(T-D/2)
        if (y-Y) < (x-X)*math.tan(arc):
            tmpans = False
        
        #上の線より上にある
        arc = math.radians(D+T/2)
        if (y-Y) > (x-X)*math.tan(arc):
            tmpans = False

        if tmpans:
            ans = True
            break
    
    ansl.append("yes" if ans else "no")

for i in range(N):
    print(ansl[i])