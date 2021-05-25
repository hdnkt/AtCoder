from bisect import bisect_right

T = int(input())

ret = []
for t in range(T):
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))

    x.sort()
    dics = {}
    for i in range(n):
        dics[x[i]]=0

    dic = []
    for i in dics:
        dic.append([i,0])

    dic.sort()

    for i in dic:
        dic[x[i]][1]=max(dic[x[i]][1],bisect_right(x,x[i]+k)-i)




print(ret)
