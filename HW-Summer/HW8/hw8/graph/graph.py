from graph.types import Edge, Node


class Graph:
    def __init__(self, edges: list[Edge] = []) -> None:
        self._adj: dict[Node, set[Node]] = {}

        self.add_edges(edges)

    def __getitem__(self, v: Node) -> set[Node]:
        """
        Return the unordered set of edges associated with node v.

        Changes to this set do not modify the underlying graph.
        """
        return self._adj[v].copy()

    def edges(self) -> list[Edge]:
        """
        Return a list of all edges in the graph.
        """
        edges = []

        for u in self._adj:
            for v in self._adj[u]:
                edges.append((u, v))

        return edges

    def add_edge(self, u: Node, v: Node) -> None:
        """
        Add an edge between node u and node v.
        """
        if u not in self._adj:
            self.add_node(u)
        if v not in self._adj:
            self.add_node(v)

        self._adj[u].add(v)
        self._adj[v].add(u)

    def add_edges(self, edges: list[Edge]) -> None:
        """
        Add edges.
        """
        for edge in edges:
            self.add_edge(*edge)

    def remove_edge(self, u: Node, v: Node) -> None:
        """
        Remove an edge between node u and node v.
        """
        self._adj[u].remove(v)
        self._adj[v].remove(u)

    def remove_edges(self, edges: list[Edge]) -> None:
        """
        Remove edges.
        """
        for edge in edges:
            self.remove_edge(*edge)

    def nodes(self) -> list[Node]:
        """
        Return a list of all nodes in the graph.

        Changes to this list do not modify the underlying graph.
        """
        return list(self._adj.keys())

    def add_node(self, v: Node) -> None:
        """
        Add node v to the graph.
        """
        self._adj[v] = set()

    def add_nodes(self, nodes: list[Node]) -> None:
        """
        Add nodes to the graph.
        """
        for node in nodes:
            self.add_node(node)

    def remove_node(self, v: Node) -> None:
        """
        Remove node v from the graph, including all associated edges.
        """
        del self._adj[v]

        for u in self._adj:
            if v in self._adj[u]:
                self._adj[u].remove(v)

    def remove_nodes(self, nodes: list[Node]) -> None:
        """
        Remove nodes from the graph, including all associated edges.
        """
        for node in nodes:
            self.remove_node(node)
