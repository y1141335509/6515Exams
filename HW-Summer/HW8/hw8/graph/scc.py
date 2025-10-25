from typing import NamedTuple

from graph.dfs import DFS, DFSOutput
from graph.digraph import DiGraph
from graph.toposort import TopoSort


class SCCOutput(NamedTuple):
    dfs: DFSOutput
    metagraph: DiGraph


def SCC(G: DiGraph) -> SCCOutput:
    result = TopoSort(G.reverse())

    GO = DiGraph()

    for node in result.order:
        GO.add_node(node)

    for u, v in G.edges():
        GO.add_edge(u, v)

    dfs = DFS(GO)

    metagraph = DiGraph()

    for cc in range(max(dfs.ccnum.values(), default=0)):
        metagraph.add_node(cc + 1)

    for u, v in GO.edges():
        if dfs.ccnum[u] != dfs.ccnum[v]:
            metagraph.add_edge(dfs.ccnum[u], dfs.ccnum[v])

    return SCCOutput(dfs, metagraph)
