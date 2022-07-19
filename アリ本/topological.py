import collections
class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.adjacent = {}
        self.visited = False
        # 入力辺のカウント
        self.in_degree = 0
        # DFSトポロジカルソートで使うマーク
        self.permanent = False
        self.temporary = False
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    def get_neighbors(self):
        return self.adjacent
    def get_connections(self):
        return self.adjacent.keys()  
    def get_vertex_id(self):
        return self.id
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    def set_visited(self):
        self.visited = True
    
    def unset_visited(self):
        self.visited = False
    
    def set_indegree(self, num):
        self.in_degree = num
    def get_indegree(self):
        return self.in_degree
class Graph(object):
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertex = 0
    
    def __iter__(self):
        return iter(self.vertex_dict.values())
    def add_vertex(self, id):
        self.num_vertex = self.num_vertex + 1
        new_vertex = Vertex(id)
        self.vertex_dict[id] = new_vertex
        return new_vertex
    def get_vertex(self, id):
        if id in self.vertex_dict:
            return self.vertex_dict[id]
        else:
            return None
    def add_edge(self, frm, to, weight=0):
        if frm not in self.vertex_dict:
            self.add_vertex(frm)
        if to not in self.vertex_dict:
            self.add_vertex(to)
        self.vertex_dict[frm].add_neighbor(self.vertex_dict[to], weight)
        # 入力辺を増やす
        self.vertex_dict[to].in_degree += 1
    def get_vertices(self):
        return self.vertex_dict.keys()
    def get_edges(self):
        edges = []
        for v in self.vertex_dict.values():
            for w in v.get_connections():
                vid = v.get_vertex_id()
                wid = w.get_vertex_id()
                edges.append((vid, wid, v.get_weight(w)))
        return edges
class GraphTopologicalError(Exception):
        pass        
def topological_sort_bfs(graph):
    # トポロジカルソートした結果を蓄積する空リスト
    topological_sorted_list = []
    queue = collections.deque()
    # 入力辺を持たないすべてのノードの集合
    for vertex in graph:
        indegree = vertex.get_indegree()
        if indegree == 0:
            queue.append(vertex)
    # while S が空ではない do
    while len(queue) > 0:
        # S からノード n を削除する
        current_vertex = queue.popleft()
        # L に n を追加する
        topological_sorted_list.append(current_vertex.get_vertex_id())
        # for each n の出力辺 e とその先のノード m do
        for neighbor in current_vertex.get_connections():
            # 辺 e をグラフから削除する
            neighbor.set_indegree(neighbor.get_indegree() - 1)
            # if m がその他の入力辺を持っていなければ then
            if neighbor.get_indegree() == 0:
                # m を S に追加する
                queue.append(neighbor)
    if len(topological_sorted_list) != len(graph.get_vertices()):
        return 0
    else:
        return topological_sorted_list

def topological_sort_dfs(graph):
    # L ← トポロジカルソートされた結果の入る空の連結リスト
    topological_reverse_sorted_list = []
    try:
        # for each ノード n do
        for current_vertex in graph:
            # if n に permanent の印が付いていない then
            if not(current_vertex.permanent):
                topological_sort_dfs_visit(current_vertex, topological_reverse_sorted_list)
    # 閉路を発見した場合
    except GraphTopologicalError:
        return [0]
    else:
        # リストは最後から読み出す
        return topological_reverse_sorted_list[::-1]
def topological_sort_dfs_visit(vertex, topological_sorted_list):
    if vertex.permanent:
        return
    # if n に「一時的」の印が付いている then
    if vertex.temporary:
        # 閉路があり DAG でないので中断
        raise GraphTopologicalError(topological_sorted_list)
    # n に「一時的」の印を付ける
    vertex.temporary = True
    # for each n の出力辺 e とその先のノード m do
    for neighbor in vertex.get_connections():
        topological_sort_dfs_visit(neighbor, topological_sorted_list)
    vertex.temprary = False
    # n に「恒久的」の印を付ける
    vertex.permanent = True
    # n を L に追加
    topological_sorted_list.append(vertex.get_vertex_id())
if __name__ == '__main__':
    n,k = map(int,input().split())
    graph = Graph()
    for i in range(0,n):
        graph.add_vertex(str(i))

    for k in range(k):
        x,y = map(int,input().split())
        graph.add_edge(str(x),str(y),1)

    #print(" ".join(map(str,topological_sort_dfs(graph))))
    ans = topological_sort_dfs(graph)
    for i in range(len(ans)):
        print(ans[i])