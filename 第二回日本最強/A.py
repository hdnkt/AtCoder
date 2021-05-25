X,Y,Z = map(int,input().split())

ans = 0
for i in range(5000000):
    ans+=1
    if ans*X >= Z*Y:
        break

print(ans-1)
