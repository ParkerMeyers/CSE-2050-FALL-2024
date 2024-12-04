class Graph:
    """
    Abstract base class for a graph. This class provides methods whose implementations
    do not depend on the underlying data structure.
    """

    def __init__(self):
        """
        Initializes the Graph class. This method should not be called directly as Graph
        is an abstract class.
        """
        raise NotImplementedError("Graph is an abstract class and should not be instantiated directly.")

    def is_connected(self, v1, v2):
        """
        Checks if there is a path between vertices v1 and v2.

        :param v1: The starting vertex.
        :param v2: The ending vertex.
        :return: True if there is a path between v1 and v2, False otherwise.
        """
        visited = set()
        queue = [v1]
        while queue:
            vertex = queue.pop(0)
            if vertex == v2:
                return True
            visited.add(vertex)
            for neighbor in self.nbrs(vertex):
                if neighbor not in visited:
                    queue.append(neighbor)
        return False

    def bfs(self, v):
        """
        Performs a breadth-first search starting from vertex v.

        :param v: The starting vertex.
        :return: A dictionary representing the BFS tree.
        """
        visited = {v: None}
        queue = [v]
        while queue:
            vertex = queue.pop(0)
            for neighbor in self.nbrs(vertex):
                if neighbor not in visited:
                    visited[neighbor] = vertex
                    queue.append(neighbor)
        return visited

    def shortest_path(self, v1, v2):
        """
        Finds the shortest path between vertices v1 and v2.

        :param v1: The starting vertex.
        :param v2: The ending vertex.
        :return: A list of vertices representing the shortest path from v1 to v2.
        """
        tree = self.bfs(v1)
        if v2 not in tree:
            return None
        path = []
        while v2 is not None:
            path.append(v2)
            v2 = tree[v2]
        return path[::-1]

    def count_trees(self):
        """
        Counts the number of distinct trees (connected components) in the graph.

        :return: A tuple containing a list of trees and the number of trees.
        """
        visited = set()
        trees = []
        for vertex in self:
            if vertex not in visited:
                tree = self.bfs(vertex)
                trees.append(tree)
                visited.update(tree.keys())
        return trees, len(trees)


class AdjacencySetGraph(Graph):
    """
    A graph implemented using an adjacency set.
    """

    def __init__(self, V=None, E=None):
        """
        Initializes the AdjacencySetGraph class.

        :param V: A list of vertices.
        :param E: A list of edges.
        """
        self._adj = {}
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for e in E:
                self.add_edge(e)

    def __iter__(self):
        """
        Returns an iterator over the vertices in the graph.

        :return: An iterator over the vertices in the graph.
        """
        return iter(self._adj)

    def add_vertex(self, v):
        """
        Adds a vertex to the graph.

        :param v: The vertex to add.
        """
        if v not in self._adj:
            self._adj[v] = set()

    def add_edge(self, e):
        """
        Adds an edge to the graph.

        :param e: A tuple (v1, v2) representing an edge between vertices v1 and v2.
        """
        v1, v2 = e
        if v1 not in self._adj or v2 not in self._adj:
            raise ValueError("Vertices not in graph: {}".format(e))
        self._adj[v1].add(v2)
        self._adj[v2].add(v1)

    def nbrs(self, v):
        """
        Returns the neighbors of a vertex.

        :param v: The vertex.
        :return: A set of neighbors of v.
        """
        if v not in self._adj:
            raise ValueError("Vertex not in graph: {}".format(v))
        return self._adj[v]


class EdgeSetGraph(Graph):
    """
    A graph implemented using an edge set.
    """

    def __init__(self, V=None, E=None):
        """
        Initializes the EdgeSetGraph with vertices V and edges E.

        :param V: A list of vertices.
        :param E: A list of edges.
        """
        self._edges = set()
        self._vertices = set()
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for e in E:
                self.add_edge(e)

    def __iter__(self):
        """
        Returns an iterator over all vertices in the graph.

        :return: An iterator over the vertices in the graph.
        """
        return iter(self._vertices)

    def add_vertex(self, v):
        """
        Adds a vertex to the graph.

        :param v: The vertex to add.
        """
        self._vertices.add(v)

    def add_edge(self, e):
        """
        Adds an edge to the graph.

        :param e: A tuple (v1, v2) representing an edge between vertices v1 and v2.
        """
        v1, v2 = e
        if v1 not in self._vertices or v2 not in self._vertices:
            raise ValueError("Vertices not in graph: {}".format(e))
        self._edges.add(e)

    def nbrs(self, v):
        """
        Returns a set of all neighbors of vertex v.

        :param v: The vertex whose neighbors are to be returned.
        :return: A set of neighbors of v.
        """
        if v not in self._vertices:
            raise ValueError("Vertex not in graph: {}".format(v))
        neighbors = set()
        for v1, v2 in self._edges:
            if v1 == v:
                neighbors.add(v2)
            elif v2 == v:
                neighbors.add(v1)
        return neighbors
