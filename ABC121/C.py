N,M = map(int,input().split())
shops = [list(map(int,input().split())) for i in range(N)]
shops.sort()
get = 0
money = 0
for i in range(0,N,1):
    if get == M:
        break
    tmp_buy = min(M-get,shops[i][1])
    get += tmp_buy
    money += tmp_buy*(shops[i][0])
print(money)
