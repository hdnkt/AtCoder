y,m,d = map(int,input().split(sep="/"))
if 4 > m:
    print("Heisei")
elif m == 4 and d <= 30:
    print("Heisei")
else:
    print("TBD")
