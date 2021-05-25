import fractions
A,B=map(int,input().split())
n =0
while n*(A-1)+1 < B:
    n+=1
print(n)
