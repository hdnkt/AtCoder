import numpy as np

N,A,B = map(int,input().split(sep=" "))
#1000でわった商、100でわった商...でもできるけどstrにする方が楽しくね

sum = 0
for i in range(1,N+1,1):
    tmp = np.array(list(map(int,list(str(i)))))
    if A<=np.sum(tmp) and np.sum(tmp)<=B:
        sum += i

print(sum)