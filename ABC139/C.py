N = int(input())
H = list(map(int,input().split())) + [10**10]

count=0
max_count=-1
for i in range(0,N,1):
    if H[i]>=H[i+1]:
        count +=1
    else:
        max_count=max(max_count,count)
        count=0
print(max_count)