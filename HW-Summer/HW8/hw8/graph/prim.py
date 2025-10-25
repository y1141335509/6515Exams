import heapq
import math

from graph.graph import Graph
from graph.types import Edge, Node


def Prim(G: Graph, weights: dict[Edge, int | float]) -> dict[Node, Node | None]:
    start = None

    cost: dict[Node, float] = {}
    prev: dict[Node, Node | None] = {}

    for node in G.nodes():
        cost[node] = math.inf
        prev[node] = None

        if start is None:
            start = node

            cost[start] = 0

    H = []

    # Increment an unused counter so that we can use mixed int | str nodes.
    count = 0
    heapq.heappush(H, (cost[start], count, start))
    count += 1

    while H:
        _, _, v = heapq.heappop(H)

        for z in G[v]:
            weight = weights.get((v, z), weights.get((z, v)))
            if cost[z] > weight:
                cost[z] = weight
                prev[z] = v

                heapq.heappush(H, (cost[z], count, z))
                count += 1

    return prev
