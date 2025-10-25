import heapq
import math
from typing import NamedTuple

from graph.graph import Graph
from graph.types import Edge, Node


class DijkstraOutput(NamedTuple):
    dist: dict[Node, int | float]
    prev: dict[Node, Node | None]


def Dijkstra(G: Graph, s: Node, lengths: dict[Edge, int | float]) -> DijkstraOutput:
    dist: dict[Node, int | float] = {}
    prev: dict[Node, Node | None] = {}

    for node in G.nodes():
        dist[node] = math.inf
        prev[node] = None

    dist[s] = 0

    H = []

    # Increment an unused counter so that we can use mixed int | str nodes.
    count = 0
    heapq.heappush(H, (dist[s], count, s))
    count += 1

    while H:
        _, _, u = heapq.heappop(H)

        for v in G[u]:
            if dist[v] > dist[u] + lengths[(u, v)]:
                dist[v] = dist[u] + lengths[(u, v)]

                prev[v] = u

                heapq.heappush(H, (dist[v], count, v))
                count += 1

    return DijkstraOutput(dist, prev)
