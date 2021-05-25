N = int(input())
G = [int(input()) for i in range(3)]

if N in G:
    print("NO")
    exit()

count =0 
while count < 100:
    if N < 4:
        N = 0
        break
    elif not(N-3 in G):
        N-=3
    elif not(N-2 in G):
        N-=2
    elif not(N-1 in G):
        N-=1
    count+=1

if N ==0:
    print("YES")
else:
    print("NO")