from typing import NamedTuple

from graph.graph import Graph
from graph.types import Node


class DFSOutput(NamedTuple):
    ccnum: dict[Node, int]
    prev: dict[Node, Node | None]
    pre: dict[Node, int]
    post: dict[Node, int]


def DFS(G: Graph) -> DFSOutput:
    cc = 1
    clock = 1

    ccnum: dict[Node, int] = {}

    pre: dict[Node, int] = {}
    post: dict[Node, int] = {}

    prev: dict[Node, Node | None] = {k: None for k in G.nodes()}

    visited = {k: False for k in G.nodes()}

    def Explore(z):
        nonlocal cc
        nonlocal clock

        ccnum[z] = cc
        visited[z] = True

        pre[z] = clock

        clock += 1

        for w in G[z]:
            if not visited[w]:
                Explore(w)

                prev[w] = z

        post[z] = clock

        clock += 1

    for v in G.nodes():
        if not visited[v]:
            Explore(v)

            cc += 1

    return DFSOutput(ccnum, prev, pre, post)
