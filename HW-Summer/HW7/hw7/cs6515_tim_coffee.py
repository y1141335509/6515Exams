from graph.digraph import DiGraph
from graph.dijkstra import Dijkstra
from graph.types import Edge, Node, Path


def reconstruct_path(prev: dict[Node, Node | None], s: Node, t: Node) -> Path:
    path = []
    curr = t
    while curr is not None:
        path.append(curr)
        curr = prev[curr]

    path.reverse()
    if path[0] == s:
        return path
    return []


def TimCoffee(
    G: DiGraph,
    s: Node,
    t: Node,
    lengths: dict[Edge, int],
    coffee_shops: dict[Node, int],
) -> tuple[Node, Path]:
    output_from_s = Dijkstra(G, s, lengths)
    dist_from_s = output_from_s.dist
    prev_from_s = output_from_s.prev   

    G_rev = G.reverse()
    rev_lengths = {(v, u): w for (u, v), w in lengths.items()}

    output_to_t = Dijkstra(G_rev, t, rev_lengths)
    dist_to_t = output_to_t.dist
    prev_to_t = output_to_t.prev

    best_shop = None
    best_cost = float('inf')

    for c, rating in coffee_shops.items():
        if dist_from_s[c] == float('inf') or dist_to_t[c] == float('inf'):
            continue
        total = dist_from_s[c] + dist_to_t[c] - rating
        if total < best_cost:
            best_cost = total
            best_shop = c

    if best_shop is None:
        return None, []
    
    path_s_to_c = reconstruct_path(prev_from_s, s, best_shop)
    path_t_to_c = reconstruct_path(prev_to_t, t, best_shop)
    path_c_to_t = list(reversed(path_t_to_c))

    path = path_s_to_c + path_c_to_t[1:]

    return best_shop, path
