from graph.graph import Graph
from graph.types import Edge


def LazyBikeRide(
    G: Graph, E_b: list[Edge], E_x: list[Edge], lengths: dict[Edge, int]
) -> list[Edge]:
    parent = {}
    rank = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x == root_y:  # same component
            return False
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True
    

    for node in G.nodes():
        parent[node] = node
        rank[node] = 0
    
    all_edges = []
    for e in E_b:
        all_edges.append((lengths[e], 0, e))
    for e in E_x:
        all_edges.append((lengths[e], 1, e))
    
    all_edges.sort(key=lambda x: (x[1], x[0]))

    result = []
    for _, _, (u, v) in all_edges:
        if union(u, v):
            result.append((u, v))
    
    return result
