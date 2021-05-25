tower = [0]*(999)
tower[0]=1
for i in range(1,999,1):
    tower[i]=tower[i-1]+(i+1)

a,b = map(int,input().split())
print(tower[b-a-1]-b)