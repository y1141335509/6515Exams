from graph.graph import Graph
from graph.types import Edge, Node


class DisjointSet:
    def __init__(self, nodes: list[Node]):
        self.__pi: dict[Node, Node] = {}
        self.__rank: dict[Node, int] = {}

        for node in nodes:
            self.__pi[node] = node
            self.__rank[node] = 0

    def find(self, x: Node) -> Node:
        if x != self.__pi[x]:
            self.__pi[x] = self.find(self.__pi[x])
        return self.__pi[x]

    def union(self, x: Node, y: Node) -> None:
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return

        if self.__rank[rx] > self.__rank[ry]:
            self.__pi[ry] = rx
        else:
            self.__pi[rx] = ry

            if self.__rank[rx] == self.__rank[ry]:
                self.__rank[ry] += 1


def Kruskal(G: Graph, weights: dict[Edge, int | float]) -> list[Edge]:
    djs = DisjointSet(G.nodes())

    X = []

    for u, v in sorted(weights, key=weights.get):
        if djs.find(u) != djs.find(v):
            X.append((u, v))
            djs.union(u, v)

    return X
