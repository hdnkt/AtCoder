import math
a,b = input().split()

n = int(a+b)

hei = False
for i in range(1,int(math.sqrt(n))+2,1):
    if i*i == n:
        hei = True
        break

print("Yes" if hei else "No")
