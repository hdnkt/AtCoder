X,N = map(int,input().split())
p = list(map(int,input().split()))

ab = 0
while 1:
    if not(X-ab in p):
        print(X-ab)
        break
    if not(X+ab in p):
        print(X+ab)
        break
    ab+=1