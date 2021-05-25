N = int(input())

#人iの出発点とゴール
AB = [list(map(int,input().split())) for i in range(N)]

kakutei = [-1]*(2*N+1)
for i in range(N):
    if AB[i][0]==-1 or AB[i][1]==-1:
        continue
    #上下おかしい弾き
    if AB[i][0] >= AB[i][1]:
        print("No")
        exit()
    #確定分
    else:
        A,B = AB[i]
        tmp = B-A-1
        if (kakutei[A]==-1 or kakutei[A]==tmp) and (kakutei[B]==-1 or kakutei[B]==tmp):
            kakutei[A]=-2
            kakutei[B]=-2
            for j in range(A+1,B):
                kakutei[j]=tmp
        else:
            print("No")
            exit()

mypredict = [[kakutei[k] for k in range(2*N+1)] for l in range(N+1)]

def solver(i,predicition):#何人目,予想
    if i == N:
        print("Yes")
        exit()

    A,B = AB[i]

    #どこでもいいを実装
    if AB[i][0]==-1 and AB[i][1]==-1:
        for a in range(0,2*N,1):
            for b in range(a+1,2*N+1,1):
                tmp = b-a-1
                if mypredict[i][a]==-1 or mypredict[i][a]==tmp:
                    if mypredict[i][b]==-1 or mypredict[i][b]==tmp:
                        for k in range(2*N+1):
                            mypredict[i+1][k]=mypredict[i][k]
                        mypredict[i+1][a]=-2
                        mypredict[i+1][b]=-2
                        for k in range(a+1,b):
                            mypredict[i+1][k]=tmp
                            solver(i+1)
    elif AB[i][0]==-1:
        for a in range(AB[i][1]-1,0,-1):
            tmp = AB[i][1]-a-1
            if mypredict[i][a]==-1 or mypredict[i][a]==tmp:
                for k in range(2*N+1):
                    mypredict[i+1][k]=mypredict[i][k]
                mypredict[i+1][a]=-2
                for k in range(a+1,AB[i][0]):
                    mypredict[i+1][k]=tmp
                solver(i+1)
                
    elif AB[i][1]==-1:
        for b in range(AB[i][0]+1,2*N+1,1):
            tmp = b-AB[i][0]-1
            if mypredict[i][b]==-1 or mypredict[i][b]==tmp:
                for k in range(2*N+1):
                    mypredict[i+1][k]=mypredict[i][k]
                mypredict[i+1][b]=-2
                for k in range(AB[i][0]+1,b):
                    mypredict[i+1][k]=tmp
                solver(i+1)


solver(0)
print("No")