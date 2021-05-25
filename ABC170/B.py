X,Y = map(int,input().split())

for i in range(0,X+1,1):
    if i*2 + (X-i)*4 == Y:
        print("Yes")
        exit()
print("No")