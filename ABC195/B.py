A,B,W = map(int,input().split())

W = W*1000

ma = W//A
if W%A != 0:
    ma += 0

mi = W//B
if W%B != 0:
    mi +=1

if mi > ma:
    print("UNSATISFIABLE")
else:
    print(mi,ma)