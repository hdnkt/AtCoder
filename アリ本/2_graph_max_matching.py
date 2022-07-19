# XとYの二部グラフの最大マッチング X={0,1,2,...|X|-1} Y={0,1,2,...,|Y|-1}
#   edges[x]: xとつながるYの頂点のset
#   matched[y]: yとマッチングされたXの頂点(暫定)
 
def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False

#初期化 X,Yがそれぞれのサイズ
#edges = [set() for _ in range(X)]
#matched = [-1] *Y
#edges[x]につながる場所を格納する
 
# 標準入力からのグラフ読み取り
N = int(input())
red_xy = [list(map(int,input().split())) for i in range(N)]
blue_xy = [list(map(int,input().split())) for i in range(N)]

edges = [set() for _ in range(N)]
matched = [-1] * N
 
for i in range(N):
    for j in range(N):
        #x, y = map(int, input().split())
        if red_xy[i][0] < blue_xy[j][0] and red_xy[i][1] < blue_xy[j][1]:
            edges[i].add(j)
 
# 増大路発見に成功したらTrue(=1)。合計することでマッチング数となる
print(sum(dfs(s, set()) for s in range(N)))