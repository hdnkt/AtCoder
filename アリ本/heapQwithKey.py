from heapq import heapify,heappush,heappop#最小（最大）の値をlogNで取り出せる。（値の追加もlogN）

a = []
heapify(a)

heappush(a,(50000,438,134455))#頭の値でヒープの処理される（頭の値が最小の物から取り出される）
heappush(a,(400,500000000,1))
print(heappop(a))

