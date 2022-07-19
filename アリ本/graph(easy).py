N = int(input())
nodes = [[] for i in range(0,N,1)]
for i in range(0,N,1):
    u,v,w = map(int,input().split())
    nodes[u].append([v,w])
    nodes[v].append([u,w])

def dfs():
    print(" ")