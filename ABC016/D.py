def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1*tc2<0 and td1*td2<0

#線分同士が交わるかをN回判定
ax,ay,bx,by = map(int,input().split())
N = int(input())
XY = [list(map(int,input().split())) for i in range(N)]

a = [ax,ay]
b = [bx,by]

ans = 0
for i in range(N):
    if intersect(XY[i],XY[(i+1)%N],a,b) == True:
        ans+=1

print(ans//2+1)

