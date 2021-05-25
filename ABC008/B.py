import collections
N = int(input())
dic = collections.defaultdict(int)

for i in range(N):
    s = input()
    dic[s]+=1

ans = "a"
num = -1
for i in dic:
    if dic[i]>num:
        ans = i
        num = dic[i]


print(ans)
