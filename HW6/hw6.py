import heapq
from collections import defaultdict


import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(V, edges, V_prime, E_prime, tree_edges):
    G = nx.Graph()
    G.add_nodes_from(V)

    edge_labels = {}
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
        edge_labels[(u, v)] = w

    pos = nx.spring_layout(G, seed=42)  # stable layout

    # Draw all edges
    default_edges = [(u, v) for u, v, _ in edges if (u, v) not in E_prime and (v, u) not in E_prime]
    dotted_edges = [(u, v) for u, v, _ in edges if (u, v) in E_prime or (v, u) in E_prime]

    nx.draw_networkx_edges(G, pos, edgelist=default_edges, width=1, edge_color="black")
    nx.draw_networkx_edges(G, pos, edgelist=dotted_edges, width=1, edge_color="gray", style="dashed")

    # Draw nodes
    V_prime_set = set(V_prime)
    color_map = ['skyblue' if v in V_prime_set else 'black' for v in V]
    nx.draw_networkx_nodes(G, pos, node_color=color_map, node_size=500)
    nx.draw_networkx_labels(G, pos, font_color='white')

    # Draw all weights
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): w for (u, v), w in edge_labels.items()})

    # Draw spanning tree on top
    T = nx.Graph()
    T.add_edges_from([(u, v) for u, v, _ in tree_edges])
    nx.draw_networkx_edges(T, pos, edgelist=T.edges(), width=3, edge_color="orange")

    plt.title("Spanning Tree (orange) with V' as leaves (blue) and dotted edges (dashed)")
    plt.axis('off')
    plt.show()



def constrained_spanning_tree(V, edges, V_prime, E_prime):
    V_set = set(V)
    V_prime = set(V_prime)
    V_core = V_set - V_prime

    E_prime_set = set(tuple(sorted(e)) for e in E_prime)

    # Step 1: Build core graph G_core = (V_core, E_core)
    E_core = []
    for u, v, w in edges:
        if u in V_core and v in V_core:
            E_core.append((w, u, v))

    # Kruskal's to get MST on core
    parent = {v: v for v in V_core}

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(u, v):
        ru, rv = find(u), find(v)
        if ru == rv: return False
        parent[rv] = ru
        return True

    mst_core = []
    E_core.sort()  # sort by weight
    for w, u, v in E_core:
        if union(u, v):
            mst_core.append((u, v, w))

    if len(mst_core) != len(V_core) - 1:
        return False  # not connected core

    # Step 2: Attach each v in V' as leaf with minimal dotted-edge use
    used_edges = list(mst_core)
    used_eprime_count = 0

    for v in V_prime:
        candidates = []
        for u, w in [(u, wt) for u, vv, wt in edges if vv == v for u2, vv2, wt2 in [(u, vv, wt)] if u in V_core] + \
                     [(vv, wt) for uu, vv, wt in edges if uu == v and vv in V_core]:
            is_dotted = (tuple(sorted((u, v))) in E_prime_set)
            candidates.append((is_dotted, w, u))  # prefer non-dotted, then smaller weight

        if not candidates:
            return False  # cannot connect this v to core

        candidates.sort()
        is_dotted, weight, u = candidates[0]
        if is_dotted:
            used_eprime_count += 1
        used_edges.append((v, u, weight))

    # Return full tree
    return used_edges, used_eprime_count



if __name__ == "__main__":
    V = list(range(8))
    edges = [
        (0, 1, 2),
        (0, 3, 3),  # dotted
        (0, 2, 6),  # dotted
        (1, 2, 2),
        (1, 5, 4),
        (2, 4, 4),
        (3, 5, 8),
        (3, 6, 5),
        (4, 5, 2),
        (4, 7, 1),
        (5, 6, 3),
        (5, 7, 3),  # dotted
        (6, 7, 5),
    ]
    V_prime = [3, 6, 7]
    E_prime = [(0, 3), (0, 2), (5, 7)]

    result = constrained_spanning_tree(V, edges, V_prime, E_prime)
    if not result:
        print("No valid tree.")
    else:
        tree_edges, dotted_used = result
        print("Tree edges:", tree_edges)
        draw_graph(V, edges, V_prime, E_prime, tree_edges)
