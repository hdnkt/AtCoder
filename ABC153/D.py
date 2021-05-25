import math
H = int(input())
n = int(math.log(H,2))
print(pow(2,n+1)-1)