import math

N = int(input())
A = [int(input())for i in range(0,5,1)]

bottol_neck = math.ceil(N/min(A))
print(bottol_neck+4)