from collections import deque 

R,W = map(int,input().split())
sy,sx = 1,1
gy,gx = R,W
C = [list(input()) for i in range(0,R,1)]

task_list = deque([])
ans = 0

siro = 0
for i in range(R):
    for j in range(W):
        if C[i][j]==".":
            siro += 1
def bfs(y,x,count):#関数にしない方がわかりやすいかも

    if x==gx-1 and y==gy-1:
        return True

    if x < 0 or  W <= x or y < 0 or R <= y:
        return False
    if C[y][x]=="#":
        return False#何もしない
    if C[y][x]==".":
        C[y][x]="#"#既に訪れたことを把握する必要あり
        task_list.append([y+1,x,count+1])
        task_list.append([y-1,x,count+1])
        task_list.append([y,x-1,count+1])
        task_list.append([y,x+1,count+1])
    

task_list.append([sy-1,sx-1,0])
ok = False
while(len(task_list)):
    y,x,t = task_list.popleft()
    ans = t
    if bfs(y,x,t):
        ok = True
        break
print(siro-1-ans if ok else -1)