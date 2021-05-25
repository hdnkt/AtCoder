N,M,D = map(int,input().split())
A = list(map(int,input().split()))

lis = list(range(N+1))
for i in range(M):
    tmp = lis[A[i]]
    lis[A[i]]=lis[A[i]+1]
    lis[A[i]+1]=tmp

ans = [0]*(N+1)
for i in range(1,N+1):
    ans[lis[i]]=i

loops = []
flags = [False]*(N+1)
for i in range(1,N+1):
    if flags[i]:
        continue
    tmp = i
    tmploops = [i]
    flags[i]=True
    while ans[tmp]!=tmploops[0]:
        tmp = ans[tmp]
        tmploops.append(tmp)
        flags[tmp]=True
    loops.append(tmploops)

ret = [0]*(N+1)
for loop in loops:
    isou = D%len(loop)
    loop=loop+loop
    for i in range(len(loop)//2):
        ret[loop[i]]=loop[i+isou]

for i in range(1,N+1):
    print(ret[i])
        