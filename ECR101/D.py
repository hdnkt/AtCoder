def dev(n,m):#ceil(n/m)
    ret = n//m
    if n%m != 0:
        ret+=1
    return ret

T = int(input())
lis = [int(input()) for i in range(T)]

for t in range(T):
    n = lis[t]
    count = 1
    tmp = 2
    for i in range(10):
        tmp=tmp*tmp
        if tmp >= n:
            break
        count+=1

    dic = {2:0,4:0,16:0,256:0,65536:0}
    de = [1,2,4,16,256,65536]
    print(n+count-2)
    for i in range(3,n):
        if not(i in dic):
            print(i,n)
    
    print(n,de[count])
    print(n,de[count])

    for i in range(count,1,-1):
        print(de[i],de[i-1])
        print(de[i],de[i-1])

