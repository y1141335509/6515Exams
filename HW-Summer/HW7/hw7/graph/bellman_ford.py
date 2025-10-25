import math
from typing import NamedTuple

from graph.graph import Graph
from graph.types import Edge, Node


class BellmanFordOutput(NamedTuple):
    dist: dict[Node, int | float]
    prev: dict[Node, Node | None]
    iter: list[dict[Node, int | float]]


def BellmanFord(
    G: Graph, s: Node, weights: dict[Edge, int | float]
) -> BellmanFordOutput:
    prev: dict[Node, Node | None] = {}
    iter: list[dict[Node, int | float]] = [{}]

    for node in G.nodes():
        prev[node] = None

        iter[0][node] = math.inf

    iter[0][s] = 0

    for i in range(1, len(G.nodes()) + 1):
        iter.append(iter[i - 1].copy())

        for u, v in G.edges():
            if iter[i][v] > iter[i - 1][u] + weights[(u, v)]:
                iter[i][v] = iter[i - 1][u] + weights[(u, v)]

                prev[v] = u

    return BellmanFordOutput(iter[-2].copy(), prev, iter)
