import numpy as np
#入力
N = int(input())
A = np.array(list(map(int,input().split(sep=" "))))

flag = True
counter = 0
while 1:
    for i in range(0,N,1):
        if A[i]%2 == 1:
            flag = False
    if flag == False:
        break
    A = A/2
    counter += 1
print(counter)