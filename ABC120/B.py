A,B,K = map(int,input().split())

wari = []
count = 0
for i in range(1,A+B):
    if A%i==0 and B%i==0:
        wari.append(i)
print(wari[len(wari)-K])
