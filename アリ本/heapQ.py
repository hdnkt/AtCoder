from heapq import heapify,heappush,heappop#最小（最大）の値をlogNで取り出せる。（値の追加もlogN）

N,L,P = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

able = True
next_petrol = 0

a=[]
heapify(a)
counter = 0
for i in range(0,L,1):
    if next_petrol < N and i == A[next_petrol]:#通過したらヒープへ
        heappush(a,-B[next_petrol])
        next_petrol +=1

    if P <= 0:
        if len(a)==0:
            exit()
        P+= -heappop(a)
        counter+=1

    P-=1

print(counter)