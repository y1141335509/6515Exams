import math
from collections import deque
from typing import NamedTuple

from graph.graph import Graph
from graph.types import Node


class BFSOutput(NamedTuple):
    dist: dict[Node, int | float]
    prev: dict[Node, Node | None]


def BFS(G: Graph, s: Node) -> BFSOutput:
    dist: dict[Node, int | float] = {}
    prev: dict[Node, Node | None] = {}

    for node in G.nodes():
        dist[node] = math.inf
        prev[node] = None

    dist[s] = 0

    Q = deque([s])

    while Q:
        u = Q.popleft()

        for v in G[u]:
            if math.isinf(dist[v]):
                dist[v] = dist[u] + 1

                prev[v] = u

                Q.append(v)

    return BFSOutput(dist, prev)
