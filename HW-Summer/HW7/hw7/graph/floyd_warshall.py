import math
from typing import NamedTuple

from graph.graph import Graph
from graph.types import Edge, Node


class FloydWarshallOutput(NamedTuple):
    dist: dict[Node, dict[Node, int | float]]
    iter: list[dict[Node, dict[Node, int | float]]]


def FloydWarshall(G: Graph, weights: dict[Edge, int | float]) -> FloydWarshallOutput:
    iter: list[dict[Node, dict[Node, int | float]]] = [{{}}]

    for s in G.nodes():
        for t in G.nodes():
            iter[0][s][t] = math.inf

    for s, t in weights:
        iter[0][s][t] = weights[(s, t)]

    row = 0

    for i in G.nodes():
        iter.append(iter[row])

        row += 1

        for s in G.nodes():
            for t in G.nodes():
                if iter[row][s][t] > iter[row][s][i] + iter[row][i][t]:
                    iter[row][s][t] = iter[row][s][i] + iter[row][i][t]

    return FloydWarshallOutput(iter[-1], iter)
