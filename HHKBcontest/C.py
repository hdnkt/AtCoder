N = int(input())
p = list(map(int,input().split()))

now = 0
dic = {}

for i in range(N):
    dic[p[i]]=0
    while now in dic:
        now+=1
    print(now) 