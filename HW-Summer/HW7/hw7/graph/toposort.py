from typing import NamedTuple

from graph.dfs import DFS, DFSOutput
from graph.digraph import DiGraph
from graph.types import Node


class TopoSortOutput(NamedTuple):
    dfs: DFSOutput
    order: list[Node]


def TopoSort(G: DiGraph) -> TopoSortOutput:
    dfs = DFS(G)

    return TopoSortOutput(dfs, sorted(dfs.post, key=dfs.post.get, reverse=True))
