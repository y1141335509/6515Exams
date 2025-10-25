from graph.graph import Graph
from graph.types import Edge, Node


class DiGraph(Graph):
    def __init__(self, edges: list[Edge] = []):
        super().__init__(edges)

    def add_edge(self, u: Node, v: Node) -> None:
        """
        Add an edge.
        """
        if u not in self._adj:
            self.add_node(u)
        if v not in self._adj:
            self.add_node(v)

        self._adj[u].add(v)

    def remove_edge(self, u: Node, v: Node) -> None:
        """
        Remove an edge from node u to node v.
        """
        self._adj[u].remove(v)

    def reverse(self):  # -> Self with Python 3.11+
        """
        Reverses the graph.
        """
        reverse = DiGraph()

        for v in self._adj:
            reverse.add_node(v)

        for u, v in self.edges():
            reverse.add_edge(v, u)

        return reverse
