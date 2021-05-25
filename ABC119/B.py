dic = {"JPY":0 , "BTC":0}
N = int(input())
for i in range(0,N,1):
    x,u = input().split()
    x = float(x)
    dic[u]+=x
print(dic["JPY"]+380000*dic["BTC"])
