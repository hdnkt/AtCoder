A = int(input())
B = int(input())
C = int(input())
dic = {A:0,B:1,C:2}
lis = [A,B,C]
lis.sort(reverse=True)

ans = [0,0,0]

for i in range(3):
    ans[dic[lis[i]]]=i

for i in range(3):
    print(ans[i]+1)
