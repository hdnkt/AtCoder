import networkx as nx
N,M,E = map(int,input().split())
p = list(map(int,input().split()))
ab = [list(map(int,input().split())) for i in range(E)]
G = nx.DiGraph()

for i in range(N):
    G.add_node(i)
G.add_node(N)
for i in range(M):
    G.add_edge(p[i],N,capacity=1)
for i in range(E):
    a,b = ab[i]
    G.add_edge(a,b,capacity=1)
    G.add_edge(b,a,capacity=1)

print(nx.minimum_cut(G,0,N)[0])



