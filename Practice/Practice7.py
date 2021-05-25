N = int(input())
a = list(map(int,input().split(sep=" ")))

AlliceTurn = True
AlliceSum = 0
BobSum = 0
while N!=0:
    maxNum = a[0]
    maxNumIndex = 0
    for i in range(0,N,1):
        if a[i] > maxNum:
            maxNum = a[i]
            maxNumIndex = i
    if AlliceTurn == True:
        AlliceSum += a.pop(maxNumIndex)
    else:
        BobSum += a.pop(maxNumIndex)
    AlliceTurn = not AlliceTurn
    N-=1
print(AlliceSum-BobSum)

