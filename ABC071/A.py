x,a,b = map(int,input().split())

disa = abs(x-a)
disb = abs(x-b)

print("A" if disa < disb else "B")