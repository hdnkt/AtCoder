import math

def kyori(x,y,x2,y2):
    return math.sqrt((x-x2)*(x-x2)+(y-y2)*(y-y2))


sx,sy,gx,gy,T,V = map(int,input().split())

n = int(input())

able = T*V

flag = False
for i in range(n):
    x,y = map(int,input().split())

    if kyori(sx,sy,x,y)+kyori(gx,gy,x,y) <= able:
        flag = True

print("YES" if flag else "NO")