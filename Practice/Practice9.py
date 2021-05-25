N,Y = map(int,input().split(sep=" "))

enable = False 
for i in range(0,N+1,1):
    for j in range(0,N+1-i,1):
            if 10000*i+5000*j+1000*(N-i-j) == Y:
                print("{} {} {}".format(i,j,N-i-j))
                enable=True
                exit()
if enable == False:
    print("-1 -1 -1")
