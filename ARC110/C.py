# 転倒数
def mergecount(A):
    cnt = 0
    n = len(A)
    if n>1:
        A1 = A[:n>>1]
        A2 = A[n>>1:]
        cnt += mergecount(A1)
        cnt += mergecount(A2)
        i1=0
        i2=0
        for i in range(n):
            if i2 == len(A2):
                A[i] = A1[i1]
                i1 += 1
            elif i1 == len(A1):
                A[i] = A2[i2]
                i2 += 1
            elif A1[i1] <= A2[i2]:
                A[i] = A1[i1]
                i1 += 1
            else:
                A[i] = A2[i2]
                i2 += 1
                cnt += n//2 - i1
    return cnt

N = int(input())
A = list(map(int,input().split()))
B = [A[i]for i in range(N)]
step = mergecount(A)

if N-1 != step:
    print(-1)
    exit()

if (N-1-step)%2 !=0:
    print(-1)
    exit()

A = [B[i]for i in range(N)]
#今いる場所をdicに保存
dic = {}
for i in range(N):
    dic[A[i]]=i
arg = [A[i] for i in range(N)]
arg.sort()
#argを下から順に見ていくと小さい順がわかる

ans = []
for i in range(N):
    #今回扱う数とその居場所
    tmp = arg[i]
    tmpnow = dic[tmp]
    while tmpnow > i:
        dic[tmp]=tmpnow-1
        dic[A[tmpnow-1]]=tmpnow
        A[tmpnow]=A[tmpnow-1]
        A[tmpnow-1]=tmp
        ans.append(tmpnow)
        tmpnow-=1

for i in range(len(ans)):
    print(ans[i])

for i in range(N-1-len(ans)):
    print(1)
