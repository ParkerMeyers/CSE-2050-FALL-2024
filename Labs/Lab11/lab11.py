class Graph_ES:
    """
    Graph implemented using an edge set.
    Vertices are stored in a set.
    Edges are stored in a set.
    """
    def __init__(self, V=None, E=None):
        """
        Initializes a graph with vertices V and edges E.
        Args:
            V (iterable): vertices
            E (iterable): edges
        """
        self.vertices = set(V) if V else set()
        self.edges = set(E) if E else set()

    def __len__(self):
        """
        Returns:
            int: number of vertices in the graph
        """
        return len(self.vertices)

    def __iter__(self):
        """
        Returns:
            iterator: iterator over the vertices in the graph
        """
        return iter(self.vertices)

    def add_vertex(self, v):
        """
        Adds a vertex to the graph.
        Args:
            v: vertex
        """
        self.vertices.add(v)

    def remove_vertex(self, v):
        """
        Removes a vertex from the graph.
        Args:
            v: vertex
        """
        if v not in self.vertices:
            raise KeyError(f"Vertex {v} not found in graph.")
        self.vertices.remove(v)
        self.edges = {e for e in self.edges if v not in e}

    def add_edge(self, e):
        """
        Adds an edge to the graph.
        Args:
            e: edge
        """
        if e[0] not in self.vertices or e[1] not in self.vertices:
            raise KeyError(f"One or both vertices {e} not found in graph.")
        self.edges.add(e)

    def remove_edge(self, e):
        """
        Removes an edge from the graph.
        Args:
            e: edge
        """
        if e not in self.edges:
            raise KeyError(f"Edge {e} not found in graph.")
        self.edges.remove(e)

    def _neighbors(self, v):
        """
        Returns an iterator over the neighbors of a vertex.
        Args:
            v: vertex
        Returns:
            iterator: iterator over the neighbors of the vertex
        """
        if v not in self.vertices:
            raise KeyError(f"Vertex {v} not found in graph.")
        return (n for u, n in self.edges if u == v)


class Graph_AS:
    """
    Graph implemented using an adjacency set.
    Vertices are stored in a set.
    Edges are stored in a dictionary with vertices as keys and sets of neighbors as values.
    """
    def __init__(self, V=None, E=None):
        """
        Initializes a graph with vertices V and edges E.
        Args:
            V (iterable): vertices
            E (iterable): edges
        """
        self.adjacency_set = {v: set() for v in (V if V else [])}
        if E:
            for u, v in E:
                self.adjacency_set[u].add(v)

    def __len__(self):
        """
        Returns:
            int: number of vertices in the graph
        """
        return len(self.adjacency_set)

    def __iter__(self):
        """
        Returns:
            iterator: iterator over the vertices in the graph
        """
        return iter(self.adjacency_set.keys())

    def add_vertex(self, v):
        """
        Adds a vertex to the graph.
        Args:
            v: vertex
        """
        if v not in self.adjacency_set:
            self.adjacency_set[v] = set()

    def remove_vertex(self, v):
        """
        Removes a vertex from the graph.
        Args:
            v: vertex
        """
        if v not in self.adjacency_set:
            raise KeyError(f"Vertex {v} not found in graph.")
        self.adjacency_set.pop(v)
        for neighbors in self.adjacency_set.values():
            neighbors.discard(v)

    def add_edge(self, e):
        """
        Adds an edge to the graph.
        Args:
            e: edge
        """
        u, v = e
        if u not in self.adjacency_set or v not in self.adjacency_set:
            raise KeyError(f"One or both vertices {e} not found in graph.")
        self.adjacency_set[u].add(v)

    def remove_edge(self, e):
        """
        Removes an edge from the graph.
        Args:
            e: edge
        """
        u, v = e
        if u not in self.adjacency_set or v not in self.adjacency_set[u]:
            raise KeyError(f"Edge {e} not found in graph.")
        self.adjacency_set[u].remove(v)

    def _neighbors(self, v):
        """
        Returns an iterator over the neighbors of a vertex.
        Args:
            v: vertex
        """
        if v not in self.adjacency_set:
            raise KeyError(f"Vertex {v} not found in graph.")
        return iter(self.adjacency_set[v])
