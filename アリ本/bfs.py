#ABC184-Eなど

from collections import deque 

R,W = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
C = [list(input()) for i in range(0,R)]


task_list = deque([])
def bfs(y,x,count):#関数にしない方がわかりやすいかも

    if x<0 or W<=x or y<0 or R<=y:
        return

    if x==gx-1 and y==gy-1:
        print(count)
        exit()

    if C[y][x]=="#":
        return#何もしない
    elif C[y][x]==".":
        C[y][x]=str(count)#既に訪れたことを把握する必要あり←これガチで大事。

        task_list.append([y+1,x,count+1])
        task_list.append([y-1,x,count+1])
        task_list.append([y,x-1,count+1])
        task_list.append([y,x+1,count+1])
    

task_list.append([sy-1,sx-1,0])
while(len(task_list)):
    y,x,t = task_list.popleft()
    bfs(y,x,t)
