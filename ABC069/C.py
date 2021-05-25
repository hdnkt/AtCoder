bai4_count=0
bai2_count=0
no = 0

N = int(input())
a = list(map(int,input().split()))

for i in range(N):
    if a[i]%4==0:
        bai4_count+=1
    elif a[i]%2==0:
        bai2_count+=1
    else:
        no+=1
ans = False
if bai2_count>0:
    if bai4_count >= no:
        ans=True
    else:
        ans=False
else:
    if bai4_count+1 >= no:
        ans=True
    else:
        ans=False

print("Yes" if ans else "No")
